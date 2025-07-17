import threading
import time
import psutil
from typing import List, Dict, Any, Iterable


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

    def poll(self) -> Dict[int, float]:
        """
        Nonblocking: for each PID, compute (now - create_time).
        If the process is gone or inaccessible, record 0.0.
        Returns the durations dict.
        """
        now = time.time()
        for pid in self.pids:  # type: ignore
            try:
                proc = psutil.Process(pid)
                self.durations[pid] = now - proc.create_time()  # type: ignore
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                self.durations[pid] = 0.0  # type: ignore
        return self.durations  # type: ignore


def flatten_process_dict(data: Dict[str, Dict[str, Dict[str, Any]]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for parent_key, children in data.items():
        # extract parent PID integer if possible
        try:
            parent_pid = int(parent_key.split("_", 1)[1])
        except ValueError:
            parent_pid = None
        for child_key, info in children.items():
            try:
                child_pid = int(child_key.split("_", 1)[1])
            except ValueError:
                continue
            row = {
                "parent_key": parent_key,
                "parent_pid": parent_pid,
                "child_key": child_key,
                "child_pid": child_pid,
                **info
            }
            out.append(row)
    return out
