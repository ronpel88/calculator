import math

# get_calc_options function return a string which contain all calc options (option in each line)
def get_calc_options():
    options = """
    1. Add   +
    2. Subtract   -
    3. Multiply   * 
    4. Divide   /
    5. Modulo   %
    6. PI   pi
    7. Help   usage
    """
    return options

# usage function return a string which contain calc usage
def usage():
    calc_usage = """calculator support the following operators:"""
    calc_usage = calc_usage + get_calc_options()
    return calc_usage

# calculate function get as parameters operation (like +/-/...) and two numbers and return a string with result
def calculate(num1, operation, num2):
    # print "num1= " + str(num1)
    # print "operation= " + str(operation)
    # print "num2= " + str(num2)

    if operation == "+":
        return str(num1) + "+" + str(num2) + "=" + str(num1+num2)
    elif operation == "-":
        return str(num1) + "-" + str(num2) + "=" + str(num1-num2)
    elif operation == "*":
        return str(num1) + "*" + str(num2) + "=" + str(num1*num2)
    elif operation == "/":
        return str(num1) + "/" + str(num2) + "=" + str(num1/num2)
    elif operation == "%":
        return str(num1) + "%" + str(num2) + "=" + str(num1%num2)
    else:
        return "Invalid input"


# main function - running first
if __name__ == '__main__':
    # display operation options to user
    print "Select operation:"
    print get_calc_options()

    # running with loop to be able to get inputs over and over
    while True:
        # get input from the user - operation
        operation = raw_input("Please enter operation:")
        if operation == "pi":
            result = math.pi
        elif operation == "usage":
            result = usage()
        else:
            # get input from the user - num1 and num2
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            # convert num1 and num2 to numerical values, as you cannot do math on strings
            int_num1 = int(num1)
            int_num2 = int(num2)
            # calculate the math and return result that contain string like: 1+1=2
            result = calculate(int_num1, operation, int_num2)
        # print result
        print result