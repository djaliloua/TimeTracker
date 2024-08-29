from datetime import datetime, timedelta
from enum import Enum


class State(Enum):
    LESS = 0
    MORE = 1


class LunchTime:
    def __init__(self,time_for_lunch: str, remaining_lunch_min: str, state: State):
        self.remaining_lunch_min = remaining_lunch_min
        self.time_for_lunch = time_for_lunch
        self.state = state


class RemainingTime:
    def __init__(self, exit_time: datetime, remaining_lunch_time: timedelta, time_spent_for_lunch:timedelta):
        self._exit_time = exit_time
        self._remaining_lunch_time = remaining_lunch_time
        self._time_spent_for_lunch = time_spent_for_lunch

    def get_exit_time(self) -> str:
        return str(self._exit_time.time().strftime("%H:%M"))

    def get_lunch_remaining_min(self) -> LunchTime:
        if "-" in str(self._remaining_lunch_time):
            return LunchTime(self._process_delta_time(self._time_spent_for_lunch),
                             str(60 - int(self._get_remaining_lunch_time())), State.MORE)

        return LunchTime(self._process_delta_time(self._time_spent_for_lunch),
                         self._get_remaining_lunch_time() ,
                         State.LESS)

    def _process_delta_time(self, value: timedelta) -> str:
        return str(value).split(":")[1]

    def _get_remaining_lunch_time(self) -> str:
        return self._process_delta_time(self._remaining_lunch_time)


