import datetime
from datetimelib.timehelper import calculate_exit_time
import flet as ft
from zucchetticontrols.headercontrol import HeaderControl
from zucchetticontrols.bodycontrol import BodyControl, RowControl
from zucchetticontrols.models import TimeModel


class BodyData(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.store_data = []
        self.data = ft.Column()
        self.callback = None
        self.f = "%Y-%m-%d %H:%M:%S.%f"
        self._load_data()

    def build(self):
        return self.data

    def _load_data(self):
        if self._is_same_date():
            self.page.client_storage.set("timesheet", [])

        if self.page.client_storage.get("timesheet") is None:
            return
        self.store_data = self.page.client_storage.get("timesheet")

        for i, dt in enumerate(self.store_data):
            if i % 2 == 0:
                self.data.controls.append(RowControl(TimeModel("entrance",
                                                               datetime.datetime.strptime(dt, self.f))))
            else:
                self.data.controls.append(RowControl(TimeModel("exit",
                                                               datetime.datetime.strptime(dt, self.f))))

        self.update()

    def add_control(self, state: str):
        tm = datetime.datetime.now()
        self.store_data.append(str(tm))
        self.page.client_storage.set("timesheet", self.store_data)
        self.data.controls.append(RowControl(TimeModel(state, tm)))
        if self.callback and self.get_count() == 3:
            self.callback()

    def get_count(self):
        return len(self.data.controls)

    def _is_same_date(self):
        t = datetime.datetime.now().strftime("%d")
        tmp = self.page.client_storage.get("timesheet")
        if tmp is None:
            return False
        if len(tmp) != 0:
            t1 = datetime.datetime.strptime(tmp[0], self.f).strftime("%d")
            if t1 != t:
                return True
        return False

    def get_entrance_count(self):
        return len([x for x in self.data.controls if x.rowdata.action == "entrance"])

    def get_exit_count(self):
        return len([x for x in self.data.controls if x.rowdata.action == "exit"])

    def compute_exit_time(self):
        if self.get_count() >= 3:
            return calculate_exit_time([x.rowdata.hour for x in self.data.controls][:3])
        return


class ZucchettiPage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.rows = BodyData(page)

    def build(self):
        return ft.Column([
            HeaderControl(self.page, self.rows),
            BodyControl(self.rows)
        ])

