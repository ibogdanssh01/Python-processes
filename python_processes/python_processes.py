""" -------------------- HEADERS -------------------- """

from pathlib import Path
import wmi
import sys
sys.path.append('../')
from python_processes.dataclasses import ProcessInfo
from python_processes.enums import ProcessType
import psutil
from pathlib import Path
import orjson


""" -------------------- HEADERS -------------------- """



""" -------------------- FUNCTIONS -------------------- """

def findPath(name: str):
    for pid in psutil.pids():
        if psutil.Process(pid).name() == name:
            return psutil.Process(pid).exe()

def printProcesses(data: dict) -> None:
    for pid, info in data.items():
        name        = info.get("name")
        abs_path    = info.get("abs_path")
        status      = info.get("status")

        print(f"Parent PID: {pid}")
        print(f"  Name    : {name}")
        print(f"  Path    : {abs_path}")
        print(f"  Status  : {status}")
        print()

def getAllProcesses() -> dict:
    data = dict()

    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            child = proc.info['pid']
            name = proc.info['name']
            status = proc.info["status"]

            if child in data:
                continue

            if child not in data:
                data[child] = {}

            data[child]["name"]        = name
            data[child]["status"]      = status
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return data

def getProcessPID() -> dict:
    data = dict()  # -> store parent pid

    for proc in psutil.process_iter(['pid', 'ppid', 'name', 'exe', 'status']):
        try:
            parent      = proc.info['ppid']
            name        = proc.info['name']
            abs_path    = proc.info['exe']
            status      = proc.info['status']

            if parent not in data:
                data[parent] = {}

            data[parent]["name"]        = name
            data[parent]["abs_path"]    = abs_path
            data[parent]["status"]      = status

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return data


def process_categorizer(process_Name: str, processID: int, time_of_creation: tuple) -> ProcessInfo:
    pass

""" -------------------- FUNCTIONS -------------------- """
