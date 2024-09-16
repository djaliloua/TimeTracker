import time

from TimeTrackerKivy.servicelocator import PlaceHolder

while counter := PlaceHolder.counter:
    min_s, secs = divmod(counter, 60)
    time_format = '{:02d}:{:02d}'.format(min_s, secs)
    print(time_format)
    counter -= 1
    time.sleep(1)
    PlaceHolder.count_down()

