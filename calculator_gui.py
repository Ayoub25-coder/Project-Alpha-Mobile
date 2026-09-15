import tkinter as tk

window = tk.Tk()

window.title("Project Alpha")
window.geometry("400x700")
title_label = tk.Label(
    window,
    text="Calculator",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=(15, 5))

display = tk.Entry(
    window,
    font=("Arial", 28),
    justify="right",
    bd=5,
    relief="sunken")
display.pack(fill="x", padx=10, pady=10)

new_calculation = False


def button_click(number):
    global new_calculation

    current = display.get()

    if new_calculation:
        display.delete(0, tk.END)
        new_calculation = False
        current = display.get()

    if number in ["+", "−", "×", "÷"]:
        if current and current[-1] in ["+", "−", "×", "÷"]:
            display.delete(len(current) - 1, tk.END)
            display.insert(tk.END, number)
            return

    if number == ".":
        parts = current.replace("−", "+").replace("×", "+").replace("÷", "+").split("+")
        
        if "." in parts[-1]:
            return

    display.insert(tk.END, number)


def square():
    current = display.get()

    if not current:
        return

    try:
        number = float(current)
        result = number ** 2

        display.delete(0, tk.END)

        if result.is_integer():
            display.insert(tk.END, int(result))
        else:
            display.insert(tk.END, result)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def square_root():
    current = display.get()

    if not current:
        return

    try:
        number = float(current)

        if number < 0:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
            return

        result = number ** 0.5

        display.delete(0, tk.END)

        if result.is_integer():
            display.insert(tk.END, int(result))
        else:
            display.insert(tk.END, result)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


def toggle_sign():
    current = display.get()

    if not current:
        return

    try:
        number = float(current)

        if number > 0:
            number = -number
        elif number < 0:
            number = abs(number)

        display.delete(0, tk.END)

        if number.is_integer():
            display.insert(tk.END, int(number))
        else:
            display.insert(tk.END, number)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        new_calculation = True


def calculate():
    global new_calculation

    expression = display.get()

    if not expression:
        return

    if expression[-1] in ["+", "−", "×", "÷"]:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        new_calculation = True
        return

    expression = expression.replace("×", "*")
    expression = expression.replace("÷", "/")
    expression = expression.replace("−", "-")

    try:
        if expression.endswith("%"):
            expression = expression[:-1]

            if "+" in expression:
                parts = expression.split("+")
                number = float(parts[0])
                percentage = float(parts[1])
                result = number + (number * percentage / 100)

            elif "-" in expression:
                parts = expression.split("-")
                number = float(parts[0])
                percentage = float(parts[1])
                result = number - (number * percentage / 100)

            else:
                number = float(expression)
                result = number / 100

        else:
            result = eval(expression)

        display.delete(0, tk.END)

        if result.is_integer():
            display.insert(tk.END, int(result))
        else:
            display.insert(tk.END, result)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

    new_calculation = True


def clear_display():
    global new_calculation

    display.delete(0, tk.END)
    new_calculation = False


def backspace():
    current = display.get()

    if current:
        display.delete(len(current) - 1, tk.END)

# Calculator buttons
button_frame = tk.Frame(window, padx=5, pady=5)
button_frame.pack()

button_7 = tk.Button(
    button_frame,
    text="7",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("7"))
button_7.grid(row=1, column=0, padx=2, pady=2)

button_8 = tk.Button(
    button_frame,
    text="8",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("8"))
button_8.grid(row=1, column=1, padx=2, pady=2)

button_9 = tk.Button(
    button_frame,
    text="9",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("9"))
button_9.grid(row=1, column=2, padx=2, pady=2)

button_4 = tk.Button(
    button_frame,
    text="4",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("4"))
button_4.grid(row=2, column=0, padx=2, pady=2)

button_5 = tk.Button(
    button_frame,
    text="5",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("5"))
button_5.grid(row=2, column=1, padx=2, pady=2)

button_6 = tk.Button(
    button_frame,
    text="6",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("6"))
button_6.grid(row=2, column=2, padx=2, pady=2)

button_1 = tk.Button(
    button_frame,
    text="1",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("1"))
button_1.grid(row=3, column=0, padx=2, pady=2)

button_2 = tk.Button(
    button_frame,
    text="2",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("2"))
button_2.grid(row=3, column=1, padx=2, pady=2)

button_3 = tk.Button(
    button_frame,
    text="3",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("3"))
button_3.grid(row=3, column=2, padx=2, pady=2)

button_0 = tk.Button(
    button_frame,
    text="0",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("0"))
button_0.grid(row=4, column=1, padx=2, pady=2)

button_dot = tk.Button(
    button_frame,
    text=".",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("."))
button_dot.grid(row=4, column=2, padx=2, pady=2)

button_divide = tk.Button(
    button_frame,
    text="÷",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("÷"))
button_divide.grid(row=1, column=3, padx=2, pady=2)

button_percent = tk.Button(
    button_frame,
    text="%",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("%"))
button_percent.grid(row=0, column=3, padx=2, pady=2)

button_multiply = tk.Button(
    button_frame,
    text="×",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("×"))
button_multiply.grid(row=2, column=3, padx=2, pady=2)

button_subtract = tk.Button(
    button_frame,
    text="−",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("−"))
button_subtract.grid(row=3, column=3, padx=2, pady=2)

button_add = tk.Button(
    button_frame,
    text="+",
    font=("Arial", 22),
    width=5,
    height=2,
    command=lambda: button_click("+"))
button_add.grid(row=4, column=3, padx=2, pady=2)

button_equals = tk.Button(
    button_frame,
    text="=",
    font=("Arial", 22),
    width=5,
    height=2,
    command=calculate)
button_equals.grid(row=5, column=3, padx=2, pady=2)

button_clear = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 22),
    width=5,
    height=2,
    command=clear_display)
button_clear.grid(row=0, column=0, padx=2, pady=2)

button_backspace = tk.Button(
    button_frame,
    text="⌫",
    font=("Arial", 22),
    width=5,
    height=2,
    command=backspace)
button_backspace.grid(row=0, column=1, padx=2, pady=2)

button_square = tk.Button(
    button_frame,
    text="x²",
    font=("Arial", 22),
    width=5,
    height=2,
    command=square)
button_square.grid(row=4, column=0, padx=2, pady=2)

button_square_root = tk.Button(
    button_frame,
    text="√",
    font=("Arial", 22),
    width=5,
    height=2,
    command=square_root)
button_square_root.grid(row=5, column=0, padx=2, pady=2)

button_plus_minus = tk.Button(
    button_frame,
    text="±",
    font=("Arial", 22),
    width=5,
    height=2,
    command=toggle_sign)
button_plus_minus.grid(row=0, column=2, padx=2, pady=2)

# Keyboard controls
def keyboard_input(event):
    key = event.keysym

    if key in ["Return", "KP_Enter"]:
        calculate()

    elif key == "BackSpace":
        backspace()

    elif key == "Escape":
        clear_display()

    elif event.char in "0123456789":
        button_click(event.char)

    elif event.char == ".":
        button_click(".")

    elif event.char == "+":
        button_click("+")

    elif event.char == "-":
        button_click("−")

    elif event.char == "*":
        button_click("×")

    elif event.char == "/":
        button_click("÷")


window.bind("<Key>", keyboard_input)

window.mainloop()