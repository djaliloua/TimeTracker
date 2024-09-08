from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.appbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationDrawerItem
from kivymd.uix.screen import MDScreen


class DrawerItem(MDNavigationDrawerItem):
    icon = StringProperty()
    text = StringProperty()
    trailing_text = StringProperty()

class Home(MDScreen):
    body_label_object = ObjectProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "home"
        self.on_kv_post = self._on_kv_post

    def _on_kv_post(self, e):
        self.ids.appbar.ids.menu_btn.bind(on_release=self._open_drawer)
        self._widget_label()

    def _open_drawer(self, instance):
        self.ids.nav_drawer.set_state("toggle")

    def _widget_label(self):
        pass

class AppBar(MDTopAppBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_kv_post = self._on_kv_post


    def _on_kv_post(self, instance):
        pass

