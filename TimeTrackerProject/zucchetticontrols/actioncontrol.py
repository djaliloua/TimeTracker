import flet as ft


class ActionControl(ft.UserControl):
    def __init__(self, usercontrol: ft.UserControl):
        super().__init__()
        self.usercontrol = usercontrol
        self.entrance_btn = ft.FilledButton("I", on_click=self._on_entrance, expand=1) #
        self.exit_btn = ft.FilledButton("O", on_click=self._on_extit, expand=1)  #
        self.name_control = ft.TextField(hint_text="your name", on_change=self._on_change, expand=2)

    def build(self):
        return ft.Row([
            self.entrance_btn,
            self.name_control,
            self.exit_btn
        ],
        alignment=ft.MainAxisAlignment.CENTER)

    def did_mount(self):
        self._initialize()

    def _initialize(self):
        self.name_control.value = self.usercontrol.page.client_storage.get("name")
        self._disable_btns_()
        self.update()

    def will_unmount(self):
        pass

    def _on_change(self, e):
        if e.data not in ("", " "):
            self.usercontrol.page.client_storage.set("name", e.data)

    def _on_entrance(self, e):
        self.usercontrol.add_control("entrance")
        self.entrance_btn.disabled = True
        self.exit_btn.disabled = False
        self._disable_btns()
        self.usercontrol.update()

    def _on_extit(self, e):
        self.usercontrol.add_control("exit")
        self.entrance_btn.disabled = False
        self.exit_btn.disabled = True
        self._disable_btns()
        self.usercontrol.update()

    def _disable_btns(self):
        if self.usercontrol.get_entrance_count() == 2:
            self.entrance_btn.disabled = True

        if self.usercontrol.get_exit_count() == 2:
            self.exit_btn.disabled = True

        if self.usercontrol.page.client_storage.get("timesheet") is not None and \
                len(self.usercontrol.page.client_storage.get("timesheet")) == 4:
            self.entrance_btn.disabled = True
            self.exit_btn.disabled = True

        self.update()

    def _disable_btns_(self):
        if self.usercontrol.get_count() == 4:
            self.entrance_btn.disabled = True
            self.exit_btn.disabled = True
        if self.usercontrol.get_count() % 2 != 0:
            self.entrance_btn.disabled = True
        else:
            self.exit_btn.disabled = True

        self.update()
