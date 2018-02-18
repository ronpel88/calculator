import math


def get_calc_options():
    options = """
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. pi
    6. Help
    """
    return options

def usage():
    calc_usage = """calculator support the following operators:"""
    calc_usage = calc_usage + get_calc_options()
    return calc_usage


def calculate(choice, num1, num2):
    print "choice= " + str(choice)
    print "num1= " + str(num1)
    print "num2= " + str(num2)

    if choice == 1:
        return str(num1) + "+" + str(num2) + "=" + str(num1+num2)
    elif choice == 2:
        return str(num1) + "-" + str(num2) + "=" + str(num1-num2)
    elif choice == 3:
        return str(num1) + "*" + str(num2) + "=" + str(num1*num2)
    elif choice == 4:
        return str(num1) + "/" + str(num2) + "=" + str(num1/num2)
    else:
        return "Invalid input"


if __name__ == '__main__':
    print "Select operation:"
    print get_calc_options()

    while True:
        # Take input from the user
        choice = input("Please enter choice:")
        if choice == 5:
            result = math.pi
        elif choice == 6:
            result = usage()
        else:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = calculate(choice, num1, num2)
        print result