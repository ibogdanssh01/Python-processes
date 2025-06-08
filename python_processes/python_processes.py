""" -------------------- HEADERS -------------------- """

import sys
sys.path.append('../')
from pathlib import Path
from python_processes.dataclasses import ProcessInfo
from python_processes.enums import ProcessType
import psutil

""" -------------------- HEADERS -------------------- """



""" -------------------- FUNCTIONS -------------------- """

def getProcessesWithParent() -> dict:
    data = dict() # -> this dictionary gonna by like that, see below
    """
    PARENT_PID: {
        CHILD_PID: {
            "name": ...
            "status": ...
            "exe" (path): ...
        }
    },
    PARENT_PID: {
        same...
    }
    """

    for proc in psutil.process_iter(['pid', 'ppid', 'name', 'status', 'exe']):
        try:
            parent_pid      = "parent_id_{}".format(proc.info['ppid'])
            child_pid       = "child_id_{}".format(proc.info['pid'])
            process_name    = proc.info['name']
            process_stats   = proc.info['status']
            process_path    = proc.info['exe']

            if parent_pid not in data:
                data[parent_pid] = {}

            if child_pid not in data[parent_pid]:
                data[parent_pid][child_pid] = {}

            data[parent_pid][child_pid]["name"] = process_name
            data[parent_pid][child_pid]["status"] = process_stats
            data[parent_pid][child_pid]["path"] = process_path
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return data


def display_process_tree(process_dict, indent=0):
    for parent_pid, children in process_dict.items():
        print("    " * indent + f"{parent_pid}: {{")
        for child_pid, info in children.items():
            print("    " * (indent + 1) + f"{child_pid}: {{")
            for key, value in info.items():
                print("    " * (indent + 2) + f'"{key}": {repr(value)}')
            print("    " * (indent + 1) + "},")
        print("    " * indent + "},")

def process_categorizer(process_Name: str, processID: int, time_of_creation: tuple) -> ProcessInfo:
    pass

""" -------------------- FUNCTIONS -------------------- """
