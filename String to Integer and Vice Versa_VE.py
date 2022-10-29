# Submitted Solution.
# Main program starts here.
def toInt(a):
    return (int(a))


def toStr(b):
    return (str(b))

# Main program ends here.
# My code after this.

## First type of input.

# Coversion to Integers.

print('Now let\'s do coversion from Strings to Integers.\n')
# Declaring the inputs here.
inputa1 = '4'
inputa2 = '5'
inputa3 = '234'
inputa4 = '234249'

print('Printing types before input.')
print(type(inputa1))
print(type(inputa2))
print(type(inputa3))
print(type(inputa4))

print('Printing after input into function.')
print(toInt(inputa1))
print(toInt(inputa2))
print(toInt(inputa3))
print(toInt(inputa4))

print('Printing types after inputting into functions.')
print(type(toInt(inputa1)))
print(type(toInt(inputa2)))
print(type(toInt(inputa3)))
print(type(toInt(inputa4)))


# Coversion to Strings.

print('Now let\'s do coversion from Integers to Strings.\n')

inputb1 = 2424
inputb2 = 525
inputb3 = 254
inputb4 = 3

print('Printing types before input.')
print(type(inputb1))
print(type(inputb2))
print(type(inputb3))
print(type(inputb4))

print('Printing after input into function.')
print(toInt(inputb1))
print(toInt(inputb2))
print(toInt(inputb3))
print(toInt(inputb4))

print('Printing types after inputting into functions.')
print(type(toInt(inputb1)))
print(type(toInt(inputb2)))
print(type(toInt(inputb3)))
print(type(toInt(inputb4)))

## Second type of input into function by Taking input from the user.

a = int(input('Please enter an number to convert str to int:\n'))
b = input('Please enter an number to convert int to str:\n')

print('Before inputting into function.')
print('Type of a:\n{}'.format(type(a)))
print('Type of b:\n{}'.format(type(b)))  # I think i will need a format specifier here.


print('After inputting into function.')
print(toInt(a))
print(toStr(b))

print('Let\'s check the type after inputting into the function.')
print(type(toInt(a)))
print(type(toInt(b)))


# I think my code ends here.

"""
Step 1 = Declaration.
Step 2 = Raw Type.
Step 3 = Input into Functions.
Step 4 = Function processed type.
*
2 (first for a and then b)
"""