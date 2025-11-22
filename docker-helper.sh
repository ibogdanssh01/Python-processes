#!/usr/bin/env bash
# docker-helper - build & run a dev container
#
# Usage:
#   docker-helper build         # build the img only
#   docker-helper run [CMD...]  # run container
#   docker-helper rebuild       # build, then run
#   docker-helper clean         # remove the image
#   docker-helper help          # this help
#
# Exit codes follow standard Unix convention:
# 0 = success, non-zero = error

set -euo pipefail

### ───────────────  CONFIGURATION  ────────────────
IMAGE_NAME="python-processes:dev"
DOCKER="$(command -v docker)" # full path, e.g., /usr/bin/docker
DOCKERFILE_DIR="$(dirname "$0")" # assume Dockerfile is in same folder


if [[ $EUID -ne 0 ]] && id -ng | grep -qw docker; then
    SUDO="sudo -n"
fi

### ───────────────────────────────

# helper: show messages in bold
log() { printf '\e[1m%s\e[0m\n' "$*"; }

usage() { grep -E '^#( |$)' "$0" | sed 's/^# \{0,1\}//'; }

build_image() {
    log "Building image "$IMAGE_NAME"..."
    "$DOCKER" build -t "$IMAGE_NAME" "$DOCKERFILE_DIR"
}

run_container() {
    log "Running image $IMAGE_NAME as root..."
    "$DOCKER" run --rm \
        --user root \
        --pid=host \
        -v "$PWD/runtime":/app/runtime \
        -e PROC_DURATIONS_PATH=/app/runtime/process_durations.json \
        -e QT_QPA_PLATFORM=offscreen \
        "$IMAGE_NAME" "$@"
}

clean_image() {
    log "Removing image "$IMAGE_NAME"..."
    "$DOCKER" rmi -f "$IMAGE_NAME" || :
}

# ───────────────────  MAIN DISPATCH  ──────────────────
case "${1:-}" in
    build)      build_image ;;
    run)        shift; run_container "$@" ;;
    rebuild)    build_image && shift && run_container "$@" ;;
    clean)      clean_image ;;
    help|-h|--help|"") usage ;;
    *)          echo "Unknown subcommand: $1" >&2; usage >&2; exit 1 ;;
esac


#### HOW TO USE IT
# chmod +x docker-helper                # make exe
# ./docker-helper build                 # build the image
# ./docker-helper run                   # run the container
# ./docker-helper rebuild               # build then run in one go
# ./docker-helper clean                 # delete the image
# ./docker-helper run python app.py     # override CMD
