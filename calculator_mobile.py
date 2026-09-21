from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorApp(App):

    def build(self):
        self.new_calculation = False

        main_layout = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=5
        )

        # Display
        self.display = Label(
             text="0",
             font_size=40,
             size_hint_y=None,
             height=100,
             halign="right",
             valign="middle"
        )
        self.display.bind(
             size=lambda instance, value:
             setattr(instance, "text_size", value)
        )
        self.display.bind(
             text=lambda instance, value:
             setattr(
                  instance,
                  "font_size",
                  max(22, min(40, 500 / max(len(value), 1)))
            )
        )

        main_layout.add_widget(self.display)

        # Calculator buttons
        buttons = [
            ["C", "DEL", "±", "%"],
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "−"],
            ["x²", "0", ".", "+"],
            ["√", "="]
        ]

        for row in buttons:
            row_layout = BoxLayout(
                orientation="horizontal",
                spacing=5
            )

            for button_text in row:
                button = Button(
                    text=button_text,
                    font_size=25
                )

                button.bind(
                    on_press=self.button_pressed
                )

                row_layout.add_widget(button)

            main_layout.add_widget(row_layout)

        return main_layout

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

        self.new_calculation = False

        if current[-1:] in ["+", "−", "×", "÷"]:
            self.display.text = current[:-1] + operator
        else:
            self.display.text += operator

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

        # Percentage
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
    # PERCENTAGE BUTTON
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
    # FORMAT RESULT
    # -------------------------

    def show_result(self, result):

        if isinstance(result, float) and result.is_integer():
            self.display.text = str(int(result))
        else:
            self.display.text = str(result)


if __name__ == "__main__":
    CalculatorApp().run()