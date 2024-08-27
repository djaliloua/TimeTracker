import flet as ft
from TimeTrackerProject.zucchetticontrols.zucchettipage import ZucchettiPage


def main(page: ft.Page):
    page.title = "Time Tracker"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    zucchettipage = ZucchettiPage(page)
    page.add(zucchettipage)


if __name__ == "__main__":
    ft.app(main)
