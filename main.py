import orjson
from pathlib import Path
import wmi
import sys
sys.path.append('../')
from gui.guiApp import App
from dictionary.order import order_by_name
from duration_logic.calculate_time import getInitTime, getClass, process_time
from time import sleep
from python_processes.python_processes import findPath
from python_processes.python_processes import get_processes, process_categorizer
import psutil

FILE_PATH = "./processes.json"

IS_RUNNING = True

if __name__ == "__main__":
    pass
