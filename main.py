
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.metrics import dp
import math


class CalculatorApp(App):

    def build(self):
        Window.clearcolor = (0.07, 0.08, 0.12, 1)
        self.expression = ""
        self.history = []
        self.answer = 0

        main = BoxLayout(
            orientation="vertical",
            padding=dp(10),
            spacing=dp(7)
        )

        title = Label(
            text="MONU SCIENTIFIC CALCULATOR",
            font_size="20sp",
            bold=True,
            size_hint_y=0.10
        )
        main.add_widget(title)

        self.display = Label(
            text="0",
            font_size="32sp",
            halign="right",
            valign="middle",
            size_hint_y=0.18
        )

        self.display.bind(
            size=lambda obj, size:
            setattr(obj, "text_size", size)
        )
        main.add_widget(self.display)

        history_title = Label(
            text="CALCULATION HISTORY",
            font_size="14sp",
            bold=True,
            size_hint_y=0.05
        )
        main.add_widget(history_title)

        self.history_display = Label(
            text="No history yet",
            font_size="13sp",
            halign="left",
            valign="middle",
            size_hint_y=0.15
        )

        self.history_display.bind(
            size=lambda obj, size:
            setattr(obj, "text_size", size)
        )
        main.add_widget(self.history_display)

        grid = GridLayout(
            cols=5,
            spacing=dp(5)
        )

        buttons = [
            "C", "⌫", "H-C", "(", ")",
            "sin", "cos", "tan", "log", "ln",
            "√", "x²", "xʸ", "π", "e",
            "7", "8", "9", "/", "%",
            "4", "5", "6", "*", "-",
            "1", "2", "3", "+", "00",
            "0", ".", "=", "Ans", "deg"
        ]

        for item in buttons:
            btn = Button(
                text=item,
                font_size="17sp",
                background_normal="",
                background_color=self.get_color(item)
            )
            btn.bind(on_press=self.button_click)
            grid.add_widget(btn)

        main.add_widget(grid)
        return main

    def get_color(self, item):

        if item == "C":
            return (0.85, 0.15, 0.20, 1)

        elif item == "=":
            return (0.10, 0.65, 0.30, 1)

        elif item == "H-C":
            return (0.85, 0.45, 0.10, 1)

        elif item in [
            "sin", "cos", "tan", "log", "ln",
            "√", "x²", "xʸ", "π", "e"
        ]:
            return (0.55, 0.25, 0.70, 1)

        elif item in ["/", "*", "-", "+", "⌫", "%"]:
            return (0.15, 0.35, 0.65, 1)

        return (0.18, 0.20, 0.28, 1)

    def update_history(self):

        if self.history:
            self.history_display.text = "\n".join(
                self.history[-5:]
            )
        else:
            self.history_display.text = "No history yet"

    def button_click(self, instance):

        value = instance.text

        if value == "H-C":
            self.history = []
            self.update_history()

        elif value == "C":
            self.expression = ""

        elif value == "⌫":
            self.expression = self.expression[:-1]

        elif value == "deg":
            self.expression += "deg("

        elif value == "π":
            self.expression += str(math.pi)

        elif value == "e":
            self.expression += str(math.e)

        elif value in ["sin", "cos", "tan", "log", "ln"]:
            self.expression += value + "("

        elif value == "√":
            self.expression += "sqrt("

        elif value == "x²":
            self.expression += "**2"

        elif value == "xʸ":
            self.expression += "**"

        elif value == "Ans":
            self.expression += str(self.answer)

        elif value == "=":

            try:
                expr = self.expression

                allowed_names = {
                    "sin": lambda x: math.sin(math.radians(x)),
                    "cos": lambda x: math.cos(math.radians(x)),
                    "tan": lambda x: math.tan(math.radians(x)),
                    "log": math.log10,
                    "ln": math.log,
                    "sqrt": math.sqrt,
                    "deg": math.radians
                }

                allowed_chars = (
                    "0123456789+-*/.() "
                    "abcdefghijklmnopqrstuvwxyz"
                )

                if not expr or not all(
                    ch in allowed_chars for ch in expr
                ):
                    raise ValueError()

                result = eval(
                    expr,
                    {"__builtins__": {}},
                    allowed_names
                )

                if not isinstance(result, (int, float)):
                    raise ValueError()

                if not math.isfinite(result):
                    raise ValueError()

                self.answer = result

                shown_result = str(round(result, 10))

                self.history.append(
                    expr + " = " + shown_result
                )

                self.update_history()
                self.expression = shown_result

            except Exception:
                self.expression = "Error"

        else:

            if self.expression == "Error":
                self.expression = ""

            self.expression += value

        self.display.text = self.expression or "0"


CalculatorApp().run()
