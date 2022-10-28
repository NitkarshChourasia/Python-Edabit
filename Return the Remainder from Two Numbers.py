# Edabit submitted solution.
# Main program starts from here.
def remainder(x,y):
    return x % y
# Main program ends here.
# My code after this.
print(remainder(4,3))
print(remainder(2,5))

# Let's test lots of modulus implemented remainders.
# Let's create a for loop until the user ends.
# UserPrompt Program is being made here.
def userinput(): # Very Faulty the while loop just keeps on going.
    # print(
    # There is a control statement like to run the loop once and then check whether the given condition is right or not?
    # It should and can be used here to make the program much more efficient, right?
    yesOrNo = input('Please input Yes or No to continue again: \n')
    yesOrNo.lower()
    if yesOrNo == 'yes' or 'y':
        while(True):
            x = int(input('Input x:\n'))
            y = int(input('Input y:\n'))
            finRem = x % y
            print('Remainder for the following integer inputs are:\n{}'.format(finRem))
            yesOrNo1 = input('Please input Yes or No to continue again: \n')
            yesOrNo1.lower()
            if yesOrNo1 == 'yes' or 'y':
                continue
            else:
                break
                # Somehow will have to iterate this while loop again.
    else:
        print('Thanks for using this program.')
# Testing scratch space.
userinput()
x = 'y'
if x == 'yes' or 'y':   # Is it a boolean or what? Like what does it output? hmm?
    print('Successful')
else:
    print('Make the program again.')