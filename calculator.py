import operator


def usage():
    print "calculator support the following operators:"
    print "1.Add"
    print "2.Subtract"
    print "3.Multiply"
    print "4.Divide"
    print "5. Help"


def calculate(choice, num1, num2):
    print "choice= " + str(choice)
    print "num1= " + str(num1)
    print "num2= " + str(num2)

    if choice == 1:
        print str(num1) + "+" + str(num2) + "=" + str(num1+num2)

    elif choice == 2:
        print str(num1) + "-" + str(num2) + "=" + str(num1-num2)

    elif choice == 3:
        print str(num1) + "*" + str(num2) + "=" + str(num1*num2)

    elif choice == 4:
        print str(num1) + "/" + str(num2) + "=" + str(num1/num2)
    else:
        print("Invalid input")


if __name__ == '__main__':
    print "Select operation."
    print "1. Add"
    print "2. Subtract"
    print "3. Multiply"
    print "4. Divide"
    print "5. Help"

    while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4/5):")
        if choice != 5:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            calculate(choice, num1, num2)
        else:
            usage()