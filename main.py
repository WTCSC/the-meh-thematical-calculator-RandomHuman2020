def add(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        added = num1 + num2
        return added
    except ValueError:
        return "fail_invalid"
def subtract(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        subtracted = num1 - num2
        return subtracted
    except ValueError:
        return "fail_invalid"
def multiply(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        multiplied = num1 * num2
        return multiplied
    except ValueError:
        return "fail_invalid"
def divide(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        if num2 == 0:
            return "fail_dividebyzero"
        else:
            divided = num1 / num2
            return divided
    except ValueError:
        return "fail_invalid"

keepgoing = True
print("I guess we're doing math now. \nGreat. \nWhat do you want to do?")

operation = input("(Valid inputs are 'add', 'subtract', 'multiply', and 'divide') ")

if operation.lower() == "add":
    success = False
    print("Oh good, you need a calculator for simple addition. \nWhat number do you want to have added to?")
    while not success:
        number1 = input("(Input any whole number.) ")
        print(f"Now, what number do you want added to {number1}?")
        number2 = input("(Input any whole number.) ")
        print(f"So, you want me to add {number2} to {number1}. \nFine.")
        if add(number1, number2) == "fail_invalid":
            print("I asked you for WHOLE NUMBERS. Not whatever that is.\nTry again.")
            success = False
        else:
            print(f"The sum of {number1} and {number2} is {add(number1, number2)}.")
            success = True
elif operation.lower() == "subtract":
    success = False
    print("Oh good, you need a calculator for simple subtraction. \nWhat number do you want to have subtracted from?")
    while not success:
        number1 = input("(Input any whole number.) ")
        print(f"Now, what number do you want subtracted from {number1}?")
        number2 = input("(Input any whole number.) ")
        print(f"So, you want me to subtract {number2} from {number1}. \nFine.")
        if add(number1, number2) == "fail_invalid":
            print("I asked you for WHOLE NUMBERS. Not whatever that is.\nTry again.")
            success = False
        else:
            print(f"The difference between {number1} and {number2} is {subtract(number1, number2)}.")
            success = True
elif operation.lower() == "multiply":
    success = False
    print("So you want me to multiply some numbers. \nI thought you had to memorise the entire multiplication table in like third grade but whatever. \nWhat number do you want to have multiplied?")
    while not success:
        number1 = input("(Input any whole number.) ")
        print(f"Now, what number do you want me to multiply {number1} by?")
        number2 = input("(Input any whole number.) ")
        print(f"So, you want me to multiply {number1} by {number2}. \nFine.")
        if add(number1, number2) == "fail_invalid":
            print("I asked you for WHOLE NUMBERS. Not whatever that is.\nTry again.")
            success = False
        else:
            print(f"The product of {number1} and {number2} is {multiply(number1, number2)}.")
            success = True
elif operation.lower() == "divide":
    success = False
    print("So you want me to divide some numbers for you.\nHonestly, that's fair.\nWhat number do you want divided?")
    while not success:
        number1 = input("(Input any whole number.) ")
        print(f"Now, what number do you want me to divide {number1} by?")
        number2 = input("(Input any whole number.)")
        print(f"So, you want me to divide {number1} by {number2}. \nOkay.")
        if divide(number1, number2) == "fail_invalid":
            print("I asked you for WHOLE NUMBERS. Not whatever that is.\nTry again.")
            success = False
        elif divide(number1, number2) == "fail_dividebyzero":
            print("Oh, you think you're soooo clever don't you? Trying to get me to do an impossible division problem.\nYou can't divide by zero.\nTry again, and don't even think about giving me another impossible equation.")
            success = False
        else:
            print(f"{number1} divided by {number2} is {divide(number1, number2)}.")
else:
    print("I have no idea what you mean by that.\nIf you just came in here to mess with me, you can go away.")
    quit("Invalid operation.")
