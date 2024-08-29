import flet as ft
from zucchetticontrols.zucchettipage import ZucchettiPage
from utility import set_value_per_platform


def main(page: ft.Page):
    page.title = "Time Tracker"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 10
    zucchettipage = ZucchettiPage(page)
    page.add(ft.Container(content=zucchettipage, margin=ft.margin.only(top=set_value_per_platform(10,89, page))))


if __name__ == "__main__":
    ft.app(main)



