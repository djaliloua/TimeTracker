from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.metrics import sp


class TimeTracker(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._app = None

    def build(self):
        # self.theme_cls.theme_style = "Light" #= ThemeManager()
        self.theme_cls.primary_palette = "Yellow"
        self._register_font_styles()

        return Builder.load_file("templates/home.kv")

    def _register_font_styles(self):
        LabelBase.register(name="custom_font", fn_regular="fonts/Debrosee-ALPnL.ttf")
        self.theme_cls.font_styles["custom_font"] = {
            "large": {
                "line-height": 1.52,
                "font-name": "custom_font",
                "font-size": sp(20)
            }
        }
        LabelBase.register(name="digital_font", fn_regular="fonts/digital-7.ttf")
        self.theme_cls.font_styles["digital_font"] = {
            "large":{
                "line-height": 1.2,
                "font-name": "digital_font",
                "font-size": sp(60)
            }
        }






if __name__ == "__main__":
    TimeTracker().run()