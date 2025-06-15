""" -------------------- HEADERS -------------------- """

import orjson
import os


""" -------------------- HEADERS -------------------- """

from src.config.global_var import FILE_PATH_PROCESSES, FILE_PATH_RULES

""" -------------------- FUNCTIONS -------------------- """

def dump_data(data: dict, FILE_PATH: str = FILE_PATH_PROCESSES) -> None:
    try:
        os.makedirs('./output', exist_ok=True)
        with open(FILE_PATH, 'wb') as f:
            f.write(orjson.dumps(data))
    except Exception as e:
        print(f"Failed to dump data: {e}")


def rule_loader(path: str = FILE_PATH_RULES) -> dict:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Rules file not found at: {path}")

    with open(path, "rb") as f:
        raw = orjson.loads(f.read())

    return {
        "system_paths": tuple(raw.get("system_paths", [])),
        "known_system_names": set(raw.get("known_system_names", []))
    }


""" -------------------- FUNCTIONS -------------------- """
