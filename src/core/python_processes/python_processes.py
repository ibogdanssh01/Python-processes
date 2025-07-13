""" -------------------- HEADERS -------------------- """

import sys
sys.path.append('../')
from src.core.python_processes.enums import ProcessType
from src.config.json_script import rule_loader
import psutil
from datetime import timedelta
import time


""" --------------------- GLOBAL VAR -----------------"""

rules = rule_loader()

""" -------------------- FUNCTIONS -------------------- """


class ProcessMonitor:
    def __init__(self):
        self.parent_name_cache: dict[int, str] = {}

    def get_processes_with_parents(self) -> dict[str, dict[str, dict]]:
        data: dict[str, dict[str, dict]] = {}

        for proc in psutil.process_iter(attrs=['pid', 'ppid', 'name', 'status', 'exe']):
            try:
                info = proc.info
                parent_key = self._get_parent_key(info['ppid'])

                child_key = f"child_{info['pid']}"
                parent_dict = data.setdefault(parent_key, {})
                parent_dict[child_key] = {
                    "name": info['name'],
                    "status": info['status'],
                    "path": info['exe'],
                    "process_type": self._get_process_category(info['exe'])
                }
            except (psutil.NoSuchProcess, psutil.AccessDenied, KeyError):
                continue
        return data

    def _get_parent_key(self, ppid: int) -> str:
        if ppid not in self.parent_name_cache:
            try:
                name = psutil.Process(ppid).name()
                self.parent_name_cache[ppid] = name.removesuffix(".exe")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                self.parent_name_cache[ppid] = "unknown"
        return f"parent_{ppid}_{self.parent_name_cache[ppid]}"

    def _get_process_category(self, path: str) -> ProcessType:
        if not path:
            return ProcessType.PROCESS_CATEGORY_SYSTEM

        path = path.lower()
        for sys_path in rules["system_paths"]:
            if sys_path in path:
                return ProcessType.PROCESS_CATEGORY_SYSTEM

        return ProcessType.PROCESS_CATEGORY_APP
