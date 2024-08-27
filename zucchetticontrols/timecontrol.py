import time
import flet as ft
import datetime


class TimeControl(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.timelbl = ft.Text(size=50)
        self.datelbl = ft.Text(size=20)

    def build(self):
        return ft.Column([
            self.datelbl,
            self.timelbl
        ])

    def _update_time(self):
        while True:
            datetime_label = datetime.datetime.now()
            self.datelbl.value = datetime_label.strftime("%A, %d %B %Y")
            self.timelbl.value = datetime_label.strftime("%H:%M:%S")
            self.update()
            time.sleep(1)

    def did_mount(self):
        self.running = True
        self.page.run_thread(self._update_time)

    def will_unmount(self):
        self.running = False
