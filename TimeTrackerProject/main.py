import flet as ft
from TimeTrackerProject.zucchetticontrols.zucchettipage import ZucchettiPage


def main(page: ft.Page):
    page.title = "Time Tracker"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 10
    zucchettipage = ZucchettiPage(page)
    page.add(ft.Container(content=zucchettipage, margin=ft.margin.only(top=80)))


if __name__ == "__main__":
    ft.app(main)



