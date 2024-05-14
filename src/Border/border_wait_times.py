from datetime import datetime


class BorderWaitTimes:
    def __init__(self, name: str):
        self.name = name
        self.wait_time = None
        self.datetime_from = None
        self.datetime_to = None

    def set_wait_time(self, wait_time) -> None:
        self.wait_time = self.format_wait_time(wait_time)

    def set_datetime(self, datetime_from, datetime_to) -> None:
        self.datetime_from = datetime_from
        self.datetime_to = datetime_to

    def get_wait_time(self) -> str:
        return self.wait_time

    def get_datetime(self) -> str:
        return f"{self.datetime_from}-{self.datetime_to}"

    def format_wait_time(self, time) -> str:
        split_time = time.split(" ")
        if split_time[1] == 'h':
            return str(int(split_time[0]) * 60) + " min"
        return time

    def validate(self) -> bool:
        if self.wait_time is None or self.datetime_from is None or self.datetime_to is None:
            return False
        return True

    def __str__(self):
        return f"{self.name},{self.wait_time},{self.datetime_from},{self.datetime_to}"