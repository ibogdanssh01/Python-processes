from dataclasses import dataclass
from python_processes.enums import ProcessType
from datetime import datetime

@dataclass
class ProcessInfo:
    """
    Represent the process info.

    ### Attributes
    - process_id: 'int = 0' - The processID
    - name: 'str = ""'      - The name of the process ex. chrome.exe
    - category: 'str = ""'  - The category of the process ex. PROCESS_CATEGORY_APP
    """
    def __init__(self, parent_id: str = None, process_id: str = None, name: str = None, category: ProcessType = ProcessType.PROCESS_CATEGORY_DEFAULT, time_of_creation: tuple = (-1, -1), full_path: str = None):
        self.parent_id: str          = parent_id
        self.process_id: str         = process_id
        self.name: str               = name
        self.category: ProcessType   = category
        self.full_path: str          = full_path
        self.time_of_creation: tuple = time_of_creation

    def __repr__(self):
        return f"ProcessInfo(id={self.process_id}), name={self.name}, category={self.category}, time_of_creation={self.time_of_creation}"