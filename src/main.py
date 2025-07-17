""" -------------------- HEADERS -------------------- """

import time
from src.core.python_processes.python_processes import ProcessMonitor
from src.config.json_script import dump_data
from time import perf_counter
from src.core.python_processes.threaded_monitor import ProcessWatcher, flatten_process_dict
from typing import List, Dict, Any
import orjson

""" -------------------- HEADERS -------------------- """

""" -------------------- GLOBAL VARIABLES --------------------"""

IS_RUNNING = True
INTERVAL_SEC = 5.0  # pause between scans
processMonitor = ProcessMonitor()

""" -------------------- GLOBAL VARIABLES --------------------"""

""" -------------------- Main --------------------"""

if __name__ == "__main__":
    while IS_RUNNING:
        t1 = perf_counter()
        print("Start...")

        nested = processMonitor.get_processes_with_parents()
        flat: List[Dict[str, Any]] = flatten_process_dict(nested)

        child_pids = [rec["child_pid"] for rec in flat]
        watcher = ProcessWatcher(child_pids)
        durations = watcher.poll()
        for rec in flat:
            rec["duration_s"] = durations.get(rec["child_pid"], 0.0)

        for rec in flat:
            rec["durations_s"] = watcher.durations.get(rec["child_pid"], 0.0)

        print("Start writing in process_durations,json...")
        with open("process_durations.json", "wb") as f:
            f.write(orjson.dumps(flat, option=orjson.OPT_INDENT_2))

        t2 = perf_counter()
        print(f"Iteration took {t2-t1:.3f} seconds")

        time.sleep(INTERVAL_SEC)
        print("Start over again....")

""" -------------------- Main --------------------"""
