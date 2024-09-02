from zucchetticontrols.zucchettipage import ZucchettiPage
import flet as ft

class BaseLocator:
    def get_singleton_control(self):
        pass

class ZucchettiPageLocator(BaseLocator):
    def __init__(self, page: ft.Page):
        self.page = page
        self._zucchetti:ZucchettiPage = None

    def get_singleton_control(self):
        if self._zucchetti:
            return self._zucchetti
        self._zucchetti = ZucchettiPage(self.page)
        return self._zucchetti
