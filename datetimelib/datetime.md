## DateTime Lib 


```from datetime import datetime
from datetimelib.models import RemainingTime
from datetimelib.timehelper import calculate_exit_time

dt = [
    datetime(2024, 8, 9, 8, 30, 0),
    datetime(2024, 8, 9, 12, 30, 0),
    datetime(2024, 8, 9, 13, 3, 0)
]

if __name__ == "__main__":
    result: RemainingTime = calculate_exit_time(dt)
    print(result.get_exit_time())
    lunch_rest = result.get_lunch_remaining_min()
    print("Remaining lunch time: ", lunch_rest.remaining_lunch_min, "min")
    print("Time spent for lunch: ", lunch_rest.time_for_lunch, "min")
    print("State: ", lunch_rest.state)
    ```