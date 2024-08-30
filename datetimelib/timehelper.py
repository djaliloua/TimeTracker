import datetime
from datetime import timedelta

from datetimelib.models import RemainingTime


def calculate_exit_time(time_sheets: list[datetime.datetime]) -> RemainingTime:
    remaining_time: RemainingTime = None
    if len(time_sheets) == 3:
        start = time_sheets[0]
        end = start + datetime.timedelta(hours=9)
        lunch_start = time_sheets[1]
        lunch_end = time_sheets[2]
        lunch_remaining = datetime.timedelta(minutes=60) - ( lunch_end - lunch_start)
        time_spent_for_lunch = lunch_end - lunch_start
        remaining_time = RemainingTime(end - lunch_remaining, lunch_remaining, time_spent_for_lunch)
    return remaining_time


def calculate_expected_lunch_time(time_sheets: list[datetime.datetime]) -> datetime:
    if len(time_sheets) == 2:
        lunch_start = time_sheets[1]
        expected_end_lunch = lunch_start + datetime.timedelta(hours=1)
        return expected_end_lunch
    return None






