# def basicCalculator(num1, operator, num2):
def basicCalculator(operator): # One way is this design another way for the upper commented function.
    # I want to learn and implement the loop function...
    # like program should go on and on until the user wants to quit.
    if operator == "*":
        a = int(input('Please input two numbers which you want to multiply:-\n'))
        b = int(input())
        print(a*b)
    elif operator == "+":
        a = int(input('Please input two numbers which you want to sum:-\n'))
        b = int(input())
        print(a+b)
    elif operator == "-":
        a = int(input('Please input two numbers which you want to substract:-\n'))
        b = int(input())
        print(a-b)
    elif operator == "/":
        a = int(input('Please input two numbers which you want to divide:-\n'))
        b = int(input())
        if b == 0:
            print('Can\'t divide by zero, Sorry bitch!')
        print(a/b)
    else:
        print('Please input a proper operator for to be calculated!')
operator = input('Please input the operator calculation you want to perform:-\n')
basicCalculator(operator)

    # See when I entered a invalid operator it ended the program ...
    # Instead I want to make a program which should prompt the user again
    # to input the data.

    # I have to absorb the ZeroDivisionError:division by zero

    # One more flaw in it is that is should function like a real calculator not
    # like a pseudo one, like it should take input like 4 * 5.
    # not the current one which you have made so , haha.
    # Let's create then...