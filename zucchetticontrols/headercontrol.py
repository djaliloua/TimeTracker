import flet as ft
from zucchetticontrols.timecontrol import TimeControl
from zucchetticontrols.actioncontrol import ActionControl


class HeaderControl(ft.UserControl):
    def __init__(self, page: ft.Page, usercontrol: ft.UserControl):
        super().__init__()
        self.page = page
        self.timectr = TimeControl(page)
        self.actionctr = ActionControl(usercontrol)

    def build(self):
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([self.timectr], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([self.actionctr], alignment=ft.MainAxisAlignment.CENTER),
                ]), margin=10
            ),
            elevation=10,
            margin=20,
            height=300
        )
