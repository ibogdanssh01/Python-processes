""" -------------------- HEADERS -------------------- """

import sys
sys.path.append('../')
from src.core.python_processes.enums import ProcessType
from src.config.json_script import rule_loader
import psutil

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

# ! TEST PURPOSE ONLY
# def display_process_tree(process_dict, indent=0):
#     for parent_pid, children in process_dict.items():
#         print("    " * indent + f"{parent_pid}: {{")
#         for child_pid, info in children.items():
#             print("    " * (indent + 1) + f"{child_pid}: {{")
#             for key, value in info.items():
#                 print("    " * (indent + 2) + f'"{key}": {repr(value)}')
#             print("    " * (indent + 1) + "},")
#         print("    " * indent + "},")


# ! TEST PURPOSE ONLY -> TODO: In this moment, in near future after a few optimization can be processes like a new feature
# def monitor_system_to_json(log_interval=2, duration=10, output_path='./output/process_log.json'):
#     log_data = []
#     start_time = time.time()

#     while time.time() - start_time < duration:
#         timestamp = datetime.now().isformat()
#         snapshot = []

#         for proc in psutil.process_iter(['pid', 'name','cpu_percent', 'memory_info']):
#             try:
#                 cpu = proc.cpu_percent(interval=0)
#                 mem = proc.info['memory_info'].rss / (1024 * 1024) # MB
#                 snapshot.append({
#                     'pid': proc.info['pid'],
#                     'name': proc.info['name'],
#                     'cpu_percent': round(cpu, 2),
#                     'memory_mb': round(mem, 2)
#                 })
#             except (psutil.NoSuchProcess, psutil.AccessDenied):
#                 continue
#         log_data.append({
#             'timestamp': timestamp,
#             'processes': snapshot
#         })

#         time.sleep(log_interval)
#         with open(output_path, 'wb') as f:
#             f.write(orjson.dumps(log_data))



# def get_process_category(path: str) -> ProcessType:
#     if not path:
#         return ProcessType.PROCESS_CATEGORY_SYSTEM

#     path = path.lower()

#     for sys_path in rules["system_paths"]:
#         if sys_path in path:
#             return ProcessType.PROCESS_CATEGORY_SYSTEM

#     return ProcessType.PROCESS_CATEGORY_APP