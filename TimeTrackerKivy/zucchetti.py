from datetime import datetime
from kivy.clock import Clock
from kivy.input.providers import platform
from kivy.properties import StringProperty, ObjectProperty
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from models import Data, TimeWrapper, Store, TimeComputation



if platform == "android":
    from plyer.platforms.android.vibrator import vibrator

store = JsonStore('time_app.json')
store.put("name", name="djalilou")


class BodyLabel(MDBoxLayout):
    def _on_kv_post(self, e):
        print(self.ids)

class BodyHeader(MDBoxLayout):
    right_label = StringProperty("right label")
    left_label = StringProperty("left label")
    def __init__(self, data: Data=Data(tm=TimeWrapper(datetime.now())), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right_label = data.time.get_time
        self.left_label = data.action

    def set_value(self, value: str) -> None:
        self.ids.right_label.text = value or ""

class TimeCard(MDCard):
    date_value = StringProperty()
    time_value = StringProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_interval(self._update, 0)


    def _update(self, dt):
        datetime_label = datetime.now()
        self.ids.date.text = datetime_label.strftime("%A, %d %B %Y")
        self.ids.tm.text = datetime_label.strftime("%H:%M:%S")

class ActionButtons(MDCard):
    text = StringProperty("hello world")
    body_object = ObjectProperty()

    def on_kv_post(self, base_widget):
        self._disable_btn(0)
        if self.body_object:
            self.body_object.load_time_sheet_data()
            self._disable_btn(self.body_object.get_number_children())


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = store.get("name")["name"]

    def on_exit(self, instance):
        if self.body_object is not None:
            if self.body_object.get_number_children() == 4:
                instance.disabled = True
                return
            count = self.body_object.add_new_entry(Data(TimeWrapper(datetime.now()), "Exit"))
            self._disable_btn(count)


    def on_entrance(self, instance):
        if self.body_object is not None:
            if self.body_object.get_number_children() == 4:
                instance.disabled = True
                return
            count = self.body_object.add_new_entry(Data(TimeWrapper(datetime.now()),"Enter"))
            self._disable_btn(count)

    def on_text(self, instance, value):
        pass

    def _disable_btn(self, n: int):
        if n == 4:
            self.ids.exit_btn.disabled = True
            self.ids.entrance_btn.disabled = True
            return
        if n % 2 == 0:
            self.ids.entrance_btn.disabled = False
            self.ids.exit_btn.disabled = True
        if n % 2 != 0:
            self.ids.entrance_btn.disabled = True
            self.ids.exit_btn.disabled = False

class Body(MDCard):
    text = StringProperty()
    body_header_control = ObjectProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.storage = Store("timesheet", "dates", [],store)
        self.time_object = TimeComputation(self.storage)
        self.f = "%Y-%m-%d %H:%M"
        self._default_time = 60*60
        self._clock_event = None
        self.body_header_control = None

    def add_new_entry(self, data: Data) -> int:
        self.ids.body_label.add_widget(BodyHeader(data))
        self.storage.save_data(data.time.get_full_date)
        self.set_time_header_label()
        if self.get_number_children() == 2:
            self._clock_event = Clock.schedule_interval(self._set_timer, 1)
        if self.get_number_children() == 3 and self._clock_event:
            self._clock_event.cancel()

        return self.get_number_children()

    def set_time_header_label(self):
        if self.body_header_control:
            self.body_header_control.ids.expected_end_lunch.set_value(self._set_exp_end_lunch())
            if result := self.time_object.compute_remaining_time():
                self.body_header_control.ids.exp_exit_time.set_value(f"{result.get_exit_time()}")
                if remaining := result.get_lunch_remaining_min():
                    self.body_header_control.ids.lunch_rem_time.set_value(f"{remaining.remaining_lunch_min} min")
                    self.body_header_control.ids.act_time_lunch.set_value(f"{remaining.time_for_lunch} min")


    def on_kv_post(self, base_widget):
        pass
        # Clock.schedule_interval(self._set_timer, 1)

    def _set_vibration_callback(self):
        if platform == "android":
            vibrator.vibrate(60)

    def _set_timer(self, dt) -> None:
        if self.body_header_control:
            if t_mer :=self.body_header_control.ids.timer:
                if self._default_time:
                    min_s, secs = divmod(self._default_time, 60)
                    time_format = '{:02d}:{:02d}'.format(min_s, secs)
                    t_mer.set_value(time_format)
                    self._default_time -= 1
                    if self._default_time == 10:
                        self._set_vibration_callback()

    def get_number_children(self) -> int:
        count = 0
        if self.ids.body_label:
            count = len(self.ids.body_label.children)
        return count

    def _set_exp_end_lunch(self):
        if obj_t := self.time_object.compute_exp_end_lunch():
            return obj_t.get_time

    def load_time_sheet_data(self):
        if self._is_same_date():
            self.storage.reset_data([])
        self.set_time_header_label()

        if self.storage.get_stored_data:
            for i, d in enumerate(self.storage.get_stored_data):
                if i % 2 == 0:
                    self.ids.body_label.add_widget(BodyHeader(Data(TimeWrapper.convert_time(d), "Enter"),))
                else:
                    self.ids.body_label.add_widget(BodyHeader(Data(TimeWrapper.convert_time(d), "Exit"), ))

    def _is_same_date(self) -> bool:
        t = datetime.now().strftime("%d")
        tmp = self.storage.get_stored_data
        if tmp is None:
            return False
        if len(tmp) != 0:
            t1 = datetime.strptime(tmp[0], self.f).strftime("%d")
            t1 = "23"
            if t1 != t:
                return True
        return False


class BodyHeaderControl(MDCard):
    pass