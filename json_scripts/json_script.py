""" -------------------- HEADERS -------------------- """

import orjson
import os


""" -------------------- HEADERS -------------------- """


""" -------------------- FUNCTIONS -------------------- """

def dump_data(data: dict) -> None:
    try:
        os.makedirs('./output', exist_ok=True)
        with open('./output/processes.json', 'wb') as f:
            f.write(orjson.dumps(data, option=orjson.OPT_INDENT_2))
    except Exception as e:
        print(f"Failed to dump data: {e}")



""" -------------------- FUNCTIONS -------------------- """
