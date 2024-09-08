from datetime import datetime
import ast
from datetimelib.models import RemainingTime
from datetimelib.timehelper import calculate_exit_time, calculate_expected_lunch_time
from kivy.storage.jsonstore import JsonStore


class TimeWrapper:
    def __init__(self, dt: datetime):
        self.format = "%Y-%m-%d %H:%M"
        self.dt = dt

    @property
    def get_full_date(self) -> str:
        return self.dt.strftime(self.format)

    @property
    def get_time(self):
        return self.dt.strftime("%H:%M")

    @staticmethod
    def convert_time(value: str):
        return TimeWrapper(datetime.strptime(value, "%Y-%m-%d %H:%M"))



class Store:
    def __init__(self, key1: str, key2: str, _store: JsonStore):
        self._store = _store
        self._key1 = key1
        self._key2 = key2


    @property
    def get_stored_data(self):
        try:
            return ast.literal_eval(self._store.get(self._key1)[self._key2])
        except:
            pass
        return []

    def reset_data(self, value):
        self._store.put(self._key1, dates=f"{value}")

    def save_data(self, value: str):
        data = self.get_stored_data
        data.append(value)
        val = {self._key2: f"{data}"}
        self._store.put(self._key1, **val)

    @property
    def count(self) -> int:
        return len(self.get_stored_data)

class Data:
    def __init__(self, tm:TimeWrapper, action: str="enter"):
        self.action = action
        self.time = tm
        self.format = "%Y-%m-%d %H:%M"


class TimeComputation:
    def __init__(self, store: Store):
        self._store = store

    def compute_exp_end_lunch(self) -> TimeWrapper:
        if self._store.count >= 2:
            d = calculate_expected_lunch_time(self._convert_[:2])
            return TimeWrapper(d)

    def compute_remaining_time(self) -> RemainingTime:
        if self._store.count >= 3:
            d = calculate_exit_time(self._convert_[:3])
            return d

    @property
    def _convert_(self):
        return [TimeWrapper.convert_time(d).dt for d in self._store.get_stored_data]

