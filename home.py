import flet as ft
from flet_core.control import Control
from servicelocator import ZucchettiPageLocator


class Home(ft.Pagelet):
    def __init__(self,page: ft.Page, content: Control):
        super().__init__(content)
        self.zucchetti_locator = ZucchettiPageLocator(page)
        self.page = page

        self.appbar = ft.AppBar(
            title=ft.Text("App"),
            bgcolor=ft.colors.LIGHT_BLUE,
            elevation=30,
            shadow_color="red"
        )

        self.content = content
        self.drawer=ft.NavigationDrawer(
            on_change=self._on_change,
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.TIME_TO_LEAVE, label="TimeTracker"
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_COMMENT, label="Item 2"
                ),
            ],
        )
        self.height = self.page.window.height
        self.txt = ft.Text(f"Selected Index changed: 1")

    def _on_change(self, e):
        if e.data == "0":
            self.content = self.zucchetti_locator.get_singleton_control()
        if e.data == "1":
            self.content = self.txt
        self.update()
        self.close_drawer()




