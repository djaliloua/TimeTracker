from datetime import datetime, timedelta
from enum import Enum


class State(Enum):
    LESS = 0
    MORE = 1


class LunchTime:
    def __init__(self, remaining_lunch_min: str, state: State):
        self.remaining_lunch_min = remaining_lunch_min
        self.state = state


class RemainingTime:
    def __init__(self, exit_time: datetime, remaining_lunch_time: timedelta):
        self._exit_time = exit_time
        self._remaining_lunch_time = remaining_lunch_time

    def get_exit_time(self) -> str:
        return str(self._exit_time.time().strftime("%H:%M"))

    def get_lunch_remaining_min(self) -> LunchTime:
        if "-" in str(self._remaining_lunch_time):
            return LunchTime(str(60 - int(str(self._remaining_lunch_time).split(":")[1])), State.MORE)

        return LunchTime(str(self._remaining_lunch_time).split(":")[1], State.LESS)
