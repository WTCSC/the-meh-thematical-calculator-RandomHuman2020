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
# some debug stuff here
operation = input("Select an operation. ")
number01 = input("Insert first number. ")
number02 = input("Insert second number. ")

if operation == "add":
    print(add(number01, number02))
elif operation == "subtract":
    print(subtract(number01, number02))
elif operation == "multiply":
    print(multiply(number01, number02))
elif operation == "divide":
    print(divide(number01, number02))