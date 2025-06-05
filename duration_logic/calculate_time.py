from collections import namedtuple
from datetime import datetime
from dataclasses import dataclass
from typing import Type, Optional, Tuple
from python_processes.dataclasses import timeClass, initTime


def getInitTime() -> Type[initTime]:
    return initTime

def getClass() -> Type[timeClass]:
    return timeClass


def process_time(
    init_time: Optional[initTime],
    actual_time: Optional[timeClass]
) -> Optional[Tuple[int, int]]:

    """
    Process_time
    Returns the difference actual_time - init_time as (hours, minutes).
    If either input is None, returns None.
    If actual_time < init_time, returns (0, 0).
    """

    if init_time is None or actual_time is None:
        return None

    start = init_time.hour * 60 + init_time.minute
    end   = actual_time.hour * 60 + actual_time.minute

    diff = end - start
    if diff < 0:
        return (0, 0)

    hours   = diff // 60
    minutes = diff % 60

    return (hours, minutes)
