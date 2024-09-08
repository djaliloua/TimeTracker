import flet as ft
from flet_core.control import Control
from aboutcontrols.about import About
from servicelocator import ZucchettiPageLocator


class Home(ft.Pagelet):
    def __init__(self,page: ft.Page, content: Control):
        super().__init__(content)
        self.zucchetti_locator = ZucchettiPageLocator(page)
        self.page = page
        self.appbar = ft.AppBar(
            title=ft.Text("App"),
            bgcolor=ft.colors.LIGHT_BLUE,
            shadow_color="green"

        )
        print(self.appbar.toolbar_height)
        self.content = content
        self.drawer=ft.NavigationDrawer(
            on_change=self._on_change,
            controls=[
                ft.NavigationDrawerDestination(
                    icon=ft.icons.TIMELAPSE, label="TimeTracker"
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.INFO, label="About"
                ),
            ],
        )
        self.height = self.page.height
        self.about = About()

    def _on_change(self, e):
        if e.data == "0":
            self.content = self.zucchetti_locator.get_singleton_control()
        if e.data == "1":
            self.content = self.about
        self.drawer.open = False
        self.drawer.update()
        self.update()

    def did_mount(self):
        pass




