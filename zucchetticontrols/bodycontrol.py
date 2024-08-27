import flet as ft

from zucchetticontrols.models import TimeModel


class RowControl(ft.UserControl):
    def __init__(self, rowdata: TimeModel):
        super().__init__()
        self.rowdata = rowdata

    def build(self):
        return ft.Row([ft.Text(self.rowdata.action),
                       ft.Text(self.rowdata.hour.time().strftime("%H:%M"))],
                      alignment=ft.MainAxisAlignment.SPACE_BETWEEN)


class BodyControl(ft.UserControl):
    def __init__(self, rows: ft.UserControl):
        super().__init__()
        rows.callback = self._on_add
        self.rows = rows
        self.remaining_lunch_time = ft.Text(f"Lunch remaining time: {self._get_remaining_lunch_time()}")
        self.expected_exit_time = ft.Text(f"Expected exit time: {self._exit_time()}",
                                          size=30)

    def build(self):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Row([ft.Text("Visualizzazione timbratura")],
                               alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([self.remaining_lunch_time],
                               alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row([self.expected_exit_time],
                               alignment=ft.MainAxisAlignment.CENTER),
                        self.rows
                    ]
                ), margin=10, padding=10
            ),
            elevation=10,
            margin=20,
            height=300
        )

    def _on_add(self):
        self.remaining_lunch_time.value = f"Lunch remaining time: {self._get_remaining_lunch_time()}"
        self.expected_exit_time.value = f"Expected exit time: {self._exit_time()}"
        self.update()

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
