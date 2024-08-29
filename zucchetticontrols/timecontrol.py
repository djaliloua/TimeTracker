import time
import flet as ft
import datetime


class TimeControl(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.time_lbl = ft.Text(size=50)
        self.date_lbl = ft.Text(size=20)
        self.controls = [
            self.date_lbl,
            self.time_lbl
        ]



    def _update_time(self):
        while True:
            datetime_label = datetime.datetime.now()
            self.date_lbl.value = datetime_label.strftime("%A, %d %B %Y")
            self.time_lbl.value = datetime_label.strftime("%H:%M:%S")
            self.update()
            time.sleep(1)

    def did_mount(self):
        self.running = True
        self.page.run_thread(self._update_time)

    def will_unmount(self):
        self.running = False
