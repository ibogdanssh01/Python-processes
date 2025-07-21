# syntax=docker/dockerfile:1
#########################################################
# 1. Builder - resolve & cache Python wheels for any arch
#########################################################
FROM --platform=$BUILDPLATFORM python:3.12-bookworm AS builder

WORKDIR /app

# -- copy dependency spec first to leverage layer-cache --
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 
COPY . .
# (requirements.txt: orjson, PyQt7, psutil, DRF, etc.) # :contentRefernece[oaicite:0]{index=0}

# -- build wheels in an isolated dir --
RUN apt-get update \
 && apt-get install -y --no-install-recommends gcc build-essential \
 && pip install --upgrade pip wheel \
 && pip wheel --wheel-dir /wheels -r requirements.txt \
 && apt-get purge -y gcc build-essential \
 && rm -rf /var/lib/apt/lists/*

# copy *all* project source for the next stage
COPY . .


#########################################################
# 2. Runtime - slim Debian + minimal Qt/X11 libs
#########################################################
FROM python:3.12-slim-bookworm

# ---- PyQt6 need the XCB plugin & GL libs ----
# (missing these results in the classic "Could not load the Qt platform plugin 'xc' ..." error) :contentReference[oaicite:1]{index=1}
RUN apt-get update && apt-get install -y --no-install-recommends \
        libegl1 \
        libfontconfig1 \
        libdbus-1-3 \
        libgl1 \
        libglib2.0-0 \
        libx11-xcb1 \
        libxkbcommon-x11-0 \
        libxcb1 libxcb-util1 libxcb-image0 libxcb-icccm4 \
        libxcb-keysyms1 libxcb-render0 libxcb-render-util0 \
        libxcb-shm0 libxcb-randr0 libxrender1 \
        fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# ---- drop root ----
RUN useradd -r -u 1001 appuser
WORKDIR /app

# ---- install pre-built wheels, no build tooling needed ----
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels

# ---- copy application source ----
COPY --from=builder /app /app

# runtime settings
ENV PYTHONUNBUFFERED=1
# Uncomment for headless execution inside CI:
# ENV QT_QPA_PLATFORM=offscreen

# give appuser ownership of everything under /app
RUN chown -R appuser:appuser /app

USER appuser

# Django REST endpoints (if enabled) default to 8000; adjust as needed
EXPOSE 8000

ENTRYPOINT [ "python", "-m", "src.main" ]


