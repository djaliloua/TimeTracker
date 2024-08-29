import flet as ft

from zucchetticontrols.bodycontrol import BodyData
from zucchetticontrols.timecontrol import TimeControl
from zucchetticontrols.actioncontrol import ActionControl


class HeaderControl(ft.Card):
    def __init__(self, page: ft.Page, usercontrol: BodyData):
        super().__init__()
        self.page = page
        self.time_ctr = TimeControl(page)
        self.action_ctr = ActionControl(usercontrol)
        self.content = ft.Container(
                content=ft.Column([
                    ft.Row([self.time_ctr], alignment=ft.MainAxisAlignment.CENTER),
                    self.action_ctr,
                ]), margin=10
            )
        self.elevation = 10
        self.height = 300
        self.margin = 20


