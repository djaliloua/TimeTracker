from kivy.lang import Builder
from kivymd.app import MDApp
from kivy import platform
from kivy.core.text import LabelBase
from kivy.metrics import sp

if platform == "android":
    from android.permissions import request_permissions, Permission
    from jnius import autoclass
    from android.runnable import run_on_ui_thread
    from android import mActivity

    View = autoclass('android.view.View')

class TimeTracker(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._app = None
        self._init_service()

    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self._register_font_styles()
        return Builder.load_file("templates/home.kv")

    def on_pause(self):
        argument = ''
        self.service.start(self.mActivity, argument)
        return True

    def on_resume(self):
        self.service.stop(self.mActivity)
        return True


    def _init_service(self):
        if platform == 'android':
            from jnius import autoclass
            self.SERVICE_NAME = u'{packagename}.Service{servicename}'.format(
                packagename=u'org.test.myapp',
                servicename=u'Myservice'
            )
            self.service = autoclass(self.SERVICE_NAME)
            self.mActivity = autoclass(u'org.kivy.android.PythonActivity').mActivity

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