import flet as ft


class About(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Markdown("### Hello world from markdown")
        self.margin = ft.margin.only(top=30, left=10)
