import orjson
from pathlib import Path
import wmi
import sys
sys.path.append('../')
from gui.guiApp import App
from dictionary.order import order_by_value
from time_package.calculate_time import getInitTime, getClass, process_time
from time import sleep


IS_RUNNING = False
FILE_PATH = "../config.json"

def get_processes() -> dict:
    processDict = dict()
    getProcess = wmi.WMI()
    for process in getProcess.Win32_Process():
        processDict[process.ProcessId] = process.Name
    return processDict

if __name__ == "__main__":
    initTime = getInitTime()
    while IS_RUNNING:
        actualTime = getClass()()
        _process_time = process_time(initTime, actualTime)
