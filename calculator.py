import math
history = []
def save_calculation(calculation):
    print(calculation)
    history.append(calculation)
    input("Press Enter to continue...")
def add():
    try:
        num1 = float(input("first number: "))
        num2 = float(input("second number: "))
    except:
        print("Invalid number. Please enter a number.")
        input("Press Enter to continue...")
        return

    result = num1 + num2
    calculation = f"{num1} + {num2} = {result:.2f}"

    save_calculation(calculation)
def subtract():
    try:
        num1 = float(input("first number: "))
        num2 = float(input("second number: "))
    except:
        print("Invalid number. Please enter a number.")
        input("Press Enter to continue...")
        return

    result = num1 - num2
    calculation = f"{num1} - {num2} = {result:.2f}"

    save_calculation(calculation)
def multiply():
    try:
        num1 = float(input("first number: "))
        num2 = float(input("second number: "))
    except:
        print("Invalid number. Please enter a number.")
        input("Press Enter to continue...")
        return

    result = num1 * num2
    calculation = f"{num1} * {num2} = {result:.2f}"

    save_calculation(calculation)
def divide():
    try:
        num1 = float(input("first number: "))
        num2 = float(input("second number: "))
    except:
        print("Invalid number. Please enter a number.")
        input("Press Enter to continue...")
        return

    try:
        result = num1 / num2
    except:
        print("You cannot divide by zero.")
        input("Press Enter to continue...")
        return
    calculation = f"{num1} / {num2} = {result:.2f}"

    save_calculation(calculation)
def square():
    try:
        num1 = float(input("Enter a number: "))
    except:
        print("Invalid number. Please enter a number.")
        input("Press Enter to continue...")
        return
    
    result = num1 ** 2
    calculation = f"{num1}² = {result:.2f}"
    save_calculation(calculation)
def square_root():
    try:
        num1 = float(input("Enter a number: "))
    except:
        print("Invalid number. Please enter a number.")
        input("Press Enter to continue...")
        return
    if num1 < 0:
        print("Cannot calculate the square root of a negative number.")
        input("Press Enter to continue...")
        return

    result = math.sqrt(num1)

    calculation = f"√{num1} = {result:.2f}"

    save_calculation(calculation)
def power():
    try:
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
    except:
        print("Invalid number. Please enter a number.")
        input("Press Enter to continue...")
        return

    result = base ** exponent

    calculation = f"{base} ^ {exponent} = {result:.2f}"

    save_calculation(calculation)
def percentage():
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter the percentage: "))
    except:
        print("Invalid number. Please enter a number.")
        input("Press Enter to continue...")
        return
    
    result = num1 * num2 / 100

    calculation = f"{num2}% of {num1} = {result:.2f}"
    
    save_calculation(calculation)

def view_history():
    print("==============================")
    print("          HISTORY")
    print("==============================")

    for number, calculation in enumerate(history, start=1):
        print(f"{number}. {calculation}")

    input("Press Enter to continue...")
def delete_history():
    if not history:
        print("History is empty.")
        input("Press Enter to continue...")
        return

    view_history()

    try:
        choice = int(input("Enter the number to delete: "))
    except:
        print("Please enter a valid number.")
        input("Press Enter to continue...")
        return
    
    if choice < 1 or choice > len(history):
        print("Invalid history number.")
        input("Press Enter to continue...")
        return
    
    history.pop(choice - 1)

    print("Calculation deleted!")
    input("Press Enter to continue...")
def clear_history():
    history.clear()
    print("History cleared!")
    input("Press Enter to continue...")
while True:
    print("==============================")
    print("      PROJECT ALPHA")
    print("        Calculator")
    print("        Version 4.1")
    print("==============================")
    print()
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    print("7. Power")
    print("8. Percentage")
    print("9. View History")
    print("10. Delete History Item")
    print("11. Clear History")
    print("12. Exit")
    
    choice = input("Enter your choice (1-12): ")
    if choice == "1":
        add()
    elif choice == "2":
        subtract()

    elif choice == "3":
        multiply()

    elif choice == "4":
        divide()

    elif choice == "5":
        square()

    elif choice == "6":
        square_root()

    elif choice == "7":
        power()

    elif choice == "8":
        percentage()

    elif choice == "9":
        view_history()

    elif choice == "10":
        delete_history()  

    elif choice == "11":
        clear_history()

    elif choice == "12":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")


