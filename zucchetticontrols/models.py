from datetime import datetime


class TimeModel:
    def __init__(self, action: str, hour: datetime):
        self.action = action
        self.hour = hour
