import flet as ft
from home import Home
from servicelocator import ZucchettiPageLocator
from zucchetticontrols.zucchettipage import ZucchettiPage
from utility import set_value_per_platform


def main(page: ft.Page):
    page.title = "Time Tracker"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 10
    zucchetti_page = ZucchettiPageLocator(page).get_singleton_control()
    home = Home(page, zucchetti_page)
    page.add(home)


if __name__ == "__main__":
    ft.app(main)



