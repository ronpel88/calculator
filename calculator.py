import math


def get_calc_options():
    options = """
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Modulo
    6. PI
    7. Help
    """
    return options

def usage():
    calc_usage = """calculator support the following operators:"""
    calc_usage = calc_usage + get_calc_options()
    return calc_usage


def calculate(operation, num1, num2):
    print "choice= " + str(operation)
    print "num1= " + str(num1)
    print "num2= " + str(num2)

    if operation == 1:
        return str(num1) + "+" + str(num2) + "=" + str(num1+num2)
    elif operation == 2:
        return str(num1) + "-" + str(num2) + "=" + str(num1-num2)
    elif operation == 3:
        return str(num1) + "*" + str(num2) + "=" + str(num1*num2)
    elif operation == 4:
        return str(num1) + "/" + str(num2) + "=" + str(num1/num2)
    elif operation == 5:
        return str(num1) + "%" + str(num2) + "=" + str(num1%num2)
    else:
        return "Invalid input"


if __name__ == '__main__':
    print "Select operation:"
    print get_calc_options()

    while True:
        # Take input from the user
        operation = input("Please enter choice:")
        if operation == 6:
            result = math.pi
        elif operation == 7:
            result = usage()
        else:
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            int_num1 = int(num1)
            int_num2 = int(num2)
            result = calculate(operation, int_num1, int_num2)
        print result