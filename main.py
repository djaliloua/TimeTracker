import flet as ft
from zucchetticontrols.zucchettipage import ZucchettiPage
from utility import set_value_per_platform


def main(page: ft.Page):
    page.title = "Time Tracker"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 10
    zucchetti_page = ZucchettiPage(page)
    page.add(ft.Container(content=zucchetti_page, margin=ft.margin.only(top=set_value_per_platform(10,50, page))))


if __name__ == "__main__":
    ft.app(main)



