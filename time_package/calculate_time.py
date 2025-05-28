from collections import namedtuple
from datetime import datetime
from dataclasses import dataclass
from typing import Type, Optional, Tuple

Constants = namedtuple('Constants', ["INIT_TIME"])
constants = Constants(INIT_TIME=datetime.now())

bool_initTime   = True
bool_actualTime = True

@dataclass
class timeClass:
    hour:   int = 0
    minute: int = 0
    second: int = 0

    def __post_init__(self):
        now = datetime.now()
        self.hour = now.hour
        self.minute = now.minute
        self.second = now.second

def getInitTime():
    return constants.INIT_TIME

def getClass() -> Type[timeClass]:
    return timeClass


"""
Process_time
Returns the difference actual_time - init_time as (hours, minutes).
If either input is None, returns None.
If actual_time < init_time, returns (0, 0).
"""

def process_time(
    init_time,
    actual_time: Optional[timeClass]
) -> Optional[Tuple[int, int]]:
    if init_time is None or actual_time is None:
        bool_initTime   = False
        bool_actualTime = False
        return None
    else:
        bool_initTime   = True
        bool_actualTime = True

    start = init_time.hour * 60 + init_time.minute
    end   = actual_time.hour * 60 + actual_time.minute

    diff = end - start
    if diff < 0:
        return (0, 0)

    hours   = diff // 60
    minutes = diff % 60
    return (hours, minutes)
