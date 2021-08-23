debug = False

def pt(my_text):
    print(my_text)


def division(num1, num2):
    if num2 == 0:
        return "Error: Cannot Divide by Zero"
    else:
        return num1/num2


def calculate(operation, num1, num2):
    if debug == True:
        print(type(num1))
        print(type(num2))
    if isinstance(num1, str) or isinstance(num1, str):
        print("cannot carry out operations on strings")
        exit(1)

    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num1 != 0 and num2 != 0:
            return num1 / num2
        else:
            print("cannot divide by zero")
            exit(1)
    else:
        print("unsupported operation")
        exit(1)


pt("hello how are you")

print(division(23, 23))

print(calculate("/", 45, 0))
