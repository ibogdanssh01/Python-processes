""" -------------------- HEADERS -------------------- """

from python_processes.python_processes import getProcessesWithParent
from json_scripts.json_script import dump_data
from time import sleep

""" -------------------- HEADERS -------------------- """

""" -------------------- GLOBAL VARIABLES --------------------"""

FILE_PATH = "./processes.json"

IS_RUNNING = True

""" -------------------- GLOBAL VARIABLES --------------------"""



""" -------------------- Main --------------------"""

if __name__ == "__main__":
    while IS_RUNNING:
        data = getProcessesWithParent()
        dump_data(data)
        sleep(2)

""" -------------------- Main --------------------"""
