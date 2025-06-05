from pathlib import Path
import wmi
import sys
sys.path.append('../')
from gui.guiApp import App
from dictionary.order import order_by_name
from duration_logic.calculate_time import getInitTime, getClass, process_time
from python_processes.dataclasses import ProcessInfo
from python_processes.enums import ProcessType
import psutil
from pathlib import Path
import orjson

def get_processes() -> dict:
    processDict = dict()
    getProcess = wmi.WMI()
    for process in getProcess.Win32_Process():
        processDict[process.ProcessId] = process.Name
    return processDict

def findPath(name):
    for pid in psutil.pids():
        if psutil.Process(pid).name() == name:
            return psutil.Process(pid).exe()


# def process_categorizer(process_Name: str, processID: int, time_of_creation: tuple) -> ProcessInfo:
def process_categorizer(FILE_PATH) -> None:
    # time_of_creation tuple (0 hour, 0 minute)
    p = Path(FILE_PATH)
    data = orjson.loads(p.read_bytes())
    dict_processes = get_processes()
    for process_id, process_name in dict_processes.items():
        process = psutil.Process(process_id)
        parent_ppid = process.ppid()
        if parent_ppid not in data.keys():
            if not process_name.endswith(".exe"):
                category = ProcessType.PROCESS_CATEGORY_WINDOWS_SYSTEM.value
            else:
                category = ProcessType.PROCESS_CATEGORY_OTHER.value
            data[str(parent_ppid)] = "({}, {})".format(process_name, category)
        else:
            error = "PPID EXIST ALREADY IN DICT"
    p.write_bytes(orjson.dumps(data))
