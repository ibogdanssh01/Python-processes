""" -------------------- HEADERS -------------------- """

import time
from src.core.python_processes.python_processes import ProcessMonitor
from src.config.json_script import dump_data
from time import perf_counter
from src.core.python_processes.threaded_monitor import ProcessWatcher, flatten_process_dict
from typing import List, Dict, Any
import orjson
from pathlib import Path
import os, signal

""" -------------------- HEADERS -------------------- """

""" -------------------- GLOBAL VARIABLES --------------------"""

IS_RUNNING = True
OUTPUT_PATH = Path(os.getenv("PROC_DURATION_PATH", "/app/runtime/process_durations.json"))
INTERVAL_SEC = float(os.getenv("INTERVAL_SEC", 5.0))
processMonitor = ProcessMonitor()
signal.signal(signal.SIGTERM, lambda *_: globals().__setitem__("IS_RUNNING", False))  
signal.signal(signal.SIGINT, lambda *_: globals().__setitem__("IS_RUNNING", False))

""" -------------------- GLOBAL VARIABLES --------------------"""

""" -------------------- Main --------------------"""

if __name__ == "__main__":
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    while IS_RUNNING:
        t1 = perf_counter()
        print("Start...")

        nested = processMonitor.get_processes_with_parents()
        flat: List[Dict[str, Any]] = flatten_process_dict(nested)

        child_pids = [rec["child_pid"] for rec in flat]
        watcher = ProcessWatcher(child_pids)
        durations = watcher.poll()
        for rec in flat:
            rec["durations_s"] = durations.get(rec["child_pid"], 0.0)

        for rec in flat:
            rec["durations_s"] = watcher.durations.get(rec["child_pid"], 0.0)

        # ---- atomic write so readers never see a half-written file ---
        tmp_path = OUTPUT_PATH.with_suffix(".tmp")
        with tmp_path.open("wb") as f:
            f.write(orjson.dumps(flat, option=orjson.OPT_INDENT_2))
            f.flush()
            os.fsync(f.fileno())
        tmp_path.replace(OUTPUT_PATH) # atomic rename on POSIX

        t2 = perf_counter()
        print(f"Iteration took {t2-t1:.3f} seconds")

        time.sleep(INTERVAL_SEC)
        print("Start over again....")
    
    print("Received signal, existing cleanly.")

""" -------------------- Main --------------------"""
