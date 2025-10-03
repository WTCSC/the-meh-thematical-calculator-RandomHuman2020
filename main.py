def add(num1, num2):
    if isinstance(num1, int):
        if isinstance(num2, int):
            added = num1 + num2
            return added
        else:
            return "fail_num2_invalid"

    else:
        return "fail_num1_invalid"
def subtract(num1, num2):
    if isinstance(num1, int):
        if isinstance(num2, int):
            subtracted = num1 - num2
            return subtracted
        else:
            return "fail_num2"
    else:
        return "fail_num1"
def multiply(num1, num2):
    if isinstance(num1, int):
        if isinstance(num2, int):
            multiplied = num1 * num2
            return multiplied
        else:
            return "fail_num2"
    else:
        return "fail_num1"
def divide(num1, num2):
    if isinstance(num1, int):
        if isinstance(num2, int):
            divided = num1 / num2
            return divided
        else:
            return "fail_num2"
    else:
        return "fail_num1"
