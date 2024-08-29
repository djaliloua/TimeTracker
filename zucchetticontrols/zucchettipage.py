import flet as ft
from zucchetticontrols.bodycontrol import BodyControl, BodyData
from zucchetticontrols.headercontrol import HeaderControl


class ZucchettiPage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.rows = BodyData(page)
        self.controls = [
            HeaderControl(self.page, self.rows),
            BodyControl(self.rows)
        ]



