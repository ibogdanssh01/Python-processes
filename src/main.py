""" -------------------- HEADERS -------------------- """

from src.core.python_processes.python_processes import ProcessMonitor
from src.config.json_script import dump_data
from time import perf_counter
""" -------------------- HEADERS -------------------- """

""" -------------------- GLOBAL VARIABLES --------------------"""

IS_RUNNING = True
processMonitor = ProcessMonitor()

""" -------------------- GLOBAL VARIABLES --------------------"""



""" -------------------- Main --------------------"""

if __name__ == "__main__":
    while IS_RUNNING:
        t1 = perf_counter()
        data = processMonitor.get_processes_with_parents()
        dump_data(data)
        t2 = perf_counter()
        print(f"{t2-t1:.3f} seconds")

""" -------------------- Main --------------------"""
