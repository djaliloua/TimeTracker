import flet as ft
from zucchetticontrols.bodycontrol import BodyControl, BodyData
from zucchetticontrols.headercontrol import HeaderControl


class ZucchettiPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.rows = BodyData(page)
        self.content = ft.Column([
            HeaderControl(self.page, self.rows),
            BodyControl(self.rows)
        ])
        self.margin = ft.margin.only(top=5)





