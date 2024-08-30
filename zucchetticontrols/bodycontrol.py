import flet as ft
import datetime

from datetimelib.models import RemainingTime
from datetimelib.timehelper import calculate_exit_time, calculate_expected_lunch_time
from zucchetticontrols.models import TimeModel


class RowControl(ft.Row):
    def __init__(self, row_data: TimeModel):
        super().__init__()
        self.row_data = row_data
        self.controls = [ft.Text(self.row_data.action),
                       ft.Text(self.row_data.hour.time().strftime("%H:%M"))]
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN

class BodyData(ft.Column):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        self.store_data = []
        self.callback = None
        self.f = "%Y-%m-%d %H:%M:%S.%f"
        self._load_data()


    def _load_data(self) -> None:
        if self._is_same_date():
            self.page.client_storage.set("timesheet", [])

        if self.page.client_storage.get("timesheet") is None:
            return
        self.store_data = self.page.client_storage.get("timesheet")

        for i, dt in enumerate(self.store_data):
            if i % 2 == 0:
                self.controls.append(RowControl(TimeModel("entrance",
                                                               datetime.datetime.strptime(dt, self.f))))
            else:
                self.controls.append(RowControl(TimeModel("exit",
                                                               datetime.datetime.strptime(dt, self.f))))


    def add_control(self, state: str) -> None:
        tm = datetime.datetime.now()
        self.store_data.append(str(tm))
        self.page.client_storage.set("timesheet", self.store_data)
        self.controls.append(RowControl(TimeModel(state, tm)))
        if self.callback and self.get_count() >= 2:
            self.callback(self.get_count())

    def get_count(self) -> int:
        return len(self.controls)

    def _is_same_date(self) -> bool:
        t = datetime.datetime.now().strftime("%d")
        tmp = self.page.client_storage.get("timesheet")
        if tmp is None:
            return False
        if len(tmp) != 0:
            t1 = datetime.datetime.strptime(tmp[0], self.f).strftime("%d")
            if t1 != t:
                return True
        return False

    def get_entrance_count(self) -> int:
        return len([x for x in self.controls if x.row_data.action == "entrance"])

    def get_exit_count(self) -> int:
        return len([x for x in self.controls if x.row_data.action == "exit"])

    def compute_exit_time(self) -> RemainingTime | None:
        if self.get_count() >= 3:
            return calculate_exit_time([x.row_data.hour for x in self.controls][:3])
        return

    def compute_expected_end_lunch_time(self) -> datetime:
        if self.get_count() >= 2:
            return calculate_expected_lunch_time([x.row_data.hour for x in self.controls][:2])
        return

class BodyControl(ft.Card):
    def __init__(self, rows: BodyData):
        super().__init__()
        rows.callback = self._on_add
        self.rows = rows
        self.remaining_lunch_time = ft.Text(f"Lunch remaining time: {self._get_remaining_lunch_time()} min")
        self.time_spent_for_lunch = ft.Text(f"Time spent for lunch: {self._get_time_spent_for_lunch()} min")
        self.expected_end_lunch = ft.Text(f"Expected end lunch: {self._get_expected_end_lunch_time()}")
        self.expected_exit_time = ft.Text(f"Expected exit time: {self._exit_time()}",
                                          size=20)
        self.content = ft.Container(
                content=ft.Column(
                    [
                        ft.Row([self.remaining_lunch_time],
                               alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([self.time_spent_for_lunch],
                               alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([self.expected_end_lunch],
                               alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([self.expected_exit_time],
                               alignment=ft.MainAxisAlignment.CENTER),
                        self.rows
                    ]
                ), margin=10, padding=10, alignment=ft.alignment.center
            )
        self.elevation = 10
        self.margin = 20
        self.height = 350

    def _on_add(self, n):
        if n == 2:
            self.expected_end_lunch.value = f"Exp. end lunch: {self._get_expected_end_lunch_time()}"
            self.update()
            return
        self.remaining_lunch_time.value = f"Lunch remaining time: {self._get_remaining_lunch_time()}"
        self.time_spent_for_lunch.value = f"Time spent for lunch: {self._get_time_spent_for_lunch()} min"
        self.expected_exit_time.value = f"Expected exit time: {self._exit_time()}"
        self.update()


    def _get_expected_end_lunch_time(self):
        if self.rows.compute_expected_end_lunch_time() is None:
            return
        return self.rows.compute_expected_end_lunch_time().strftime("%H:%M")

    def _get_remaining_lunch_time(self):
        if self.rows.compute_exit_time() is None:
            return
        return self.rows\
            .compute_exit_time()\
            .get_lunch_remaining_min()\
            .remaining_lunch_min if self.rows\
            .compute_exit_time()\
            .get_lunch_remaining_min() is not None else None

    def _exit_time(self):
        if self.rows.compute_exit_time() is None:
            return
        return self.rows.compute_exit_time().get_exit_time()

    def _get_time_spent_for_lunch(self):
        if self.rows.compute_exit_time() is None:
            return
        return self.rows\
            .compute_exit_time()\
            .get_lunch_remaining_min()\
            .time_for_lunch if self.rows\
            .compute_exit_time()\
            .get_lunch_remaining_min() is not None else None

