import flet as ft

def set_value_per_platform(w_value, android_value, page: ft.Page):
    return w_value if page.platform == ft.PagePlatform.WINDOWS else android_value