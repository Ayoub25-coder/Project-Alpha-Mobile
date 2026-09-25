from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


# Desktop testing size only
from kivy.utils import platform

if platform == "win":
    Window.size = (400, 750)


class CalculatorButton(Button):
    button_color = ListProperty([0.15, 0.15, 0.18, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)
        self.color = (1, 1, 1, 1)
        self.font_size = dp(24)

        with self.canvas.before:
            self.bg_color = Color(*self.button_color)
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(14)]
            )

        self.bind(pos=self.update_background)
        self.bind(size=self.update_background)
        self.bind(button_color=self.update_color)

    def update_background(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def update_color(self, *args):
        self.bg_color.rgb = self.button_color[:3]
        self.bg_color.a = self.button_color[3]


class CalculatorApp(App):

    def build(self):
        self.new_calculation = False

        main_layout = BoxLayout(
            orientation="vertical",
            padding=dp(12),
            spacing=dp(8)
        )

        # -------------------------
        # DISPLAY
        # -------------------------

        display_box = BoxLayout(
             orientation="vertical",
             size_hint_y=None,
             height=dp(105),
             padding=[dp(10), dp(2)]
        )

        title = Label(
             text="PROJECT ALPHA",
             font_size=dp(14),
             color=(0.65, 0.65, 0.70, 1),
             size_hint_y=None,
             height=dp(25),
             halign="right",
             valign="middle"
        )

        title.bind(
             size=lambda instance, value:
             setattr(instance, "text_size", value)
        )

        display_box.add_widget(title)

        self.display = Label(
            text="0",
            font_size=dp(42),
            color=(1, 1, 1, 1),
            halign="right",
            valign="middle"
        )

        self.display.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        self.display.bind(
            text=self.adjust_font_size
        )

        display_box.add_widget(self.display)
        main_layout.add_widget(display_box)

        # -------------------------
        # BUTTON ROWS
        # -------------------------

        buttons = [
            [("C", [0.75, 0.20, 0.20, 1]),
             ("DEL", [0.35, 0.35, 0.40, 1]),
             ("±", [0.35, 0.35, 0.40, 1]),
             ("%", [0.35, 0.35, 0.40, 1])],

            [("7", None), ("8", None), ("9", None),
             ("÷", [0.95, 0.55, 0.15, 1])],

            [("4", None), ("5", None), ("6", None),
             ("×", [0.95, 0.55, 0.15, 1])],

            [("1", None), ("2", None), ("3", None),
             ("−", [0.95, 0.55, 0.15, 1])],

            [("x²", [0.25, 0.30, 0.45, 1]),
             ("0", None),
             (".", None),
             ("+", [0.95, 0.55, 0.15, 1])]
        ]

        for row in buttons:
            row_layout = BoxLayout(
                orientation="horizontal",
                spacing=dp(7)
            )

            for text, color in row:

                if color is None:
                    color = [0.15, 0.15, 0.18, 1]

                button = CalculatorButton(
                    text=text,
                    button_color=color
                )

                button.bind(
                    on_press=self.button_pressed
                )

                row_layout.add_widget(button)

            main_layout.add_widget(row_layout)

        # -------------------------
        # BOTTOM ROW
        # -------------------------

        bottom_row = BoxLayout(
            orientation="horizontal",
            spacing=dp(7)
        )

        sqrt_button = CalculatorButton(
            text="√",
            button_color=[0.25, 0.30, 0.45, 1]
        )

        equal_button = CalculatorButton(
            text="=",
            button_color=[0.95, 0.55, 0.15, 1]
        )

        sqrt_button.bind(
            on_press=self.button_pressed
        )

        equal_button.bind(
            on_press=self.button_pressed
        )

        bottom_row.add_widget(sqrt_button)
        bottom_row.add_widget(equal_button)

        main_layout.add_widget(bottom_row)

        return main_layout

    # -------------------------
    # DISPLAY FONT
    # -------------------------

    def adjust_font_size(self, instance, value):
        length = len(value)

        if length <= 10:
            instance.font_size = dp(42)
        elif length <= 14:
            instance.font_size = dp(34)
        elif length <= 18:
            instance.font_size = dp(28)
        else:
            instance.font_size = dp(23)

    # -------------------------
    # BUTTON HANDLER
    # -------------------------

    def button_pressed(self, instance):
        button = instance.text

        if button in "0123456789":
            self.number(button)

        elif button == ".":
            self.decimal()

        elif button in ["+", "−", "×", "÷"]:
            self.operator(button)

        elif button == "=":
            self.calculate()

        elif button == "C":
            self.clear()

        elif button == "DEL":
            self.delete()

        elif button == "±":
            self.toggle_sign()

        elif button == "%":
            self.percentage()

        elif button == "x²":
            self.square()

        elif button == "√":
            self.square_root()

    # -------------------------
    # NUMBERS
    # -------------------------

    def number(self, number):
        current = self.display.text

        if self.new_calculation or current == "0":
            self.display.text = number
            self.new_calculation = False
        else:
            self.display.text += number

    # -------------------------
    # DECIMAL
    # -------------------------

    def decimal(self):
        current = self.display.text

        if self.new_calculation:
            self.display.text = "0."
            self.new_calculation = False
            return

        parts = (
            current
            .replace("−", "+")
            .replace("×", "+")
            .replace("÷", "+")
            .split("+")
        )

        if "." not in parts[-1]:
            self.display.text += "."

    # -------------------------
    # OPERATORS
    # -------------------------

    def operator(self, operator):
        current = self.display.text

        if current == "Error":
            return

        if current[-1:] in ["+", "−", "×", "÷"]:
            self.display.text = current[:-1] + operator
        else:
            self.display.text += operator

        self.new_calculation = False

    # -------------------------
    # CALCULATE
    # -------------------------

    def calculate(self):
        expression = self.display.text

        if not expression or expression == "Error":
            return

        if expression[-1:] in ["+", "−", "×", "÷"]:
            self.display.text = "Error"
            self.new_calculation = True
            return

        if expression.endswith("%"):
            expression = expression[:-1]

            try:
                if "+" in expression:
                    parts = expression.split("+")
                    number = float(parts[0])
                    percentage = float(parts[1])
                    result = number + (number * percentage / 100)

                elif "−" in expression:
                    parts = expression.split("−")
                    number = float(parts[0])
                    percentage = float(parts[1])
                    result = number - (number * percentage / 100)

                else:
                    number = float(expression)
                    result = number / 100

                self.show_result(result)

            except:
                self.display.text = "Error"

            self.new_calculation = True
            return

        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")
        expression = expression.replace("−", "-")

        try:
            result = eval(expression)
            self.show_result(result)

        except:
            self.display.text = "Error"

        self.new_calculation = True

    # -------------------------
    # SQUARE
    # -------------------------

    def square(self):
        try:
            number = float(self.display.text)
            result = number ** 2
            self.show_result(result)
            self.new_calculation = True

        except:
            self.display.text = "Error"
            self.new_calculation = True

    # -------------------------
    # SQUARE ROOT
    # -------------------------

    def square_root(self):
        try:
            number = float(self.display.text)

            if number < 0:
                self.display.text = "Error"
                self.new_calculation = True
                return

            result = number ** 0.5
            self.show_result(result)
            self.new_calculation = True

        except:
            self.display.text = "Error"
            self.new_calculation = True

    # -------------------------
    # PLUS / MINUS
    # -------------------------

    def toggle_sign(self):
        try:
            number = float(self.display.text)
            number = -number
            self.show_result(number)

        except:
            self.display.text = "Error"

    # -------------------------
    # PERCENTAGE
    # -------------------------

    def percentage(self):
        current = self.display.text

        if current and current[-1] not in ["+", "−", "×", "÷", "%"]:
            self.display.text += "%"

    # -------------------------
    # DELETE
    # -------------------------

    def delete(self):
        current = self.display.text

        if current and current != "Error":
            self.display.text = current[:-1]

            if self.display.text == "":
                self.display.text = "0"

    # -------------------------
    # CLEAR
    # -------------------------

    def clear(self):
        self.display.text = "0"
        self.new_calculation = False

    # -------------------------
    # RESULT FORMAT
    # -------------------------

    def show_result(self, result):

        if isinstance(result, float) and result.is_integer():
            self.display.text = str(int(result))
        else:
            self.display.text = str(result)


if __name__ == "__main__":
    CalculatorApp().run()