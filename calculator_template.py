
# get_calc_options function return a string which contain all calc options (option in each line)
def get_calc_options():
    options = ""
    return options

# usage function return a string which contain calc usage
def usage():
    # crete string that contain all operations that are supported in calculator
    calc_usage = ""
    calc_usage = calc_usage + get_calc_options()
    return calc_usage

# calculate function get as parameters operation (like +/-/...) and two numbers and return a string with result
def calculate(num1, operation, num2):
    # go over all operation options - and each operation return string that contain result
    return "2+2=4"


# main function - running first
if __name__ == '__main__':
    # display operation options to user
    print "Select operation:"
    print get_calc_options()

    # get input from the user - operation
    operation = "+"
    if operation == "pi":
        # if user asked to get pi value - print pi value using math library
        result = "pi is 3.14..."
    elif operation == "usage":
        # if user asked to get usage - print calc usage using usage function
        result = "usage"
    else:
        # get input from the user - num1 and num2
        num1 = "2"
        num2 = "2"
        # convert num1 and num2 to numerical values, as you cannot do math on strings
        int_num1 = 2
        int_num2 = 2
        # calculate the math and return result that contain string (like: 1+1=2), using calculate function
        result = calculate(int_num1, operation, int_num2)
    # print result
    print result