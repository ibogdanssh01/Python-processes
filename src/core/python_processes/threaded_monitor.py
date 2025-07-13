import threading
import time
import psutil
from typing import Iterable, Dict

class ProcessWatcher:
    """Watch multiple processes and record how long they ran."""
    
    def __init__(self, pids: Iterable[int]):
        self.pids = list(pids)
        self.start_times: Dict[int, float] = {}
        self.durations: Dict[int, float] = {}
        self._threads: list[threading.Thread] = []
        
    def _watch(self, pid: int) -> None:
        start = time.perf_counter()
        self.start_times[pid] = start
        try:
            psutil.Process(pid).wait()
        except psutil.NoSuchProcess:
            pass
        finally:
            self.durations[pid] = time.perf_counter() - start
    
    def start(self) -> None:
        for pid in self.pids:
            t = threading.Thread(target=self._watch, args=(pid,), daemon=True)
            self._threads.append(t)
            t.start()
    
    def join(self) -> None:
        for thread in self._threads:
            thread.join() 