from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.metrics import dp, sp


class CalcApp(App):
    def build(self):
        self._update_metrics()

        root = GridLayout(cols=1, padding=self.pad, spacing=self.spacing)

        self.display = Label(
            text="0",
            font_size=self.display_fs,
            halign="right",
            valign="middle",
            size_hint_y=0.22,
        )
        self.display.bind(size=self._update_display_text_size)
        root.add_widget(self.display)

        self.grid = GridLayout(cols=4, spacing=self.spacing)
        root.add_widget(self.grid)

        self.buttons = []
        layout = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '⌫'],
        ]
        for row in layout:
            for label in row:
                btn = Button(text=label, font_size=self.button_fs)
                btn.bind(on_press=self.on_press)
                self.grid.add_widget(btn)
                self.buttons.append(btn)

        Window.bind(size=self.on_window_resize)

        self.expression = ""
        return root

    def _update_metrics(self):
        w, h = Window.size
        base = min(w, h)
        self.pad = max(dp(4), base * 0.02)
        self.spacing = max(dp(4), base * 0.015)
        self.display_fs = max(sp(24), base * 0.10)
        self.button_fs = max(sp(14), base * 0.06)

    def _update_display_text_size(self, *args):
        self.display.text_size = self.display.size

    def on_window_resize(self, window, size):
        self._update_metrics()
        self.display.font_size = self.display_fs
        for btn in self.buttons:
            btn.font_size = self.button_fs

    def on_press(self, instance):
        t = instance.text
        if t == 'C':
            self.expression = ""
        elif t == '⌫':
            self.expression = self.expression[:-1]
        elif t == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Erreur"
        else:
            self.expression += t

        self.display.text = self.expression or "0"
        self._auto_shrink_display()

    def _auto_shrink_display(self):
        base_fs = self.display_fs
        text_len = len(self.display.text)
        max_chars = max(1, int(self.display.width / (base_fs * 0.6)))
        if text_len > max_chars:
            self.display.font_size = max(sp(12), base_fs * max_chars / text_len)
        else:
            self.display.font_size = base_fs


if __name__ == "__main__":
    CalcApp().run()
