# Edabit submitted solution:
# Main program starts here.
def convert(hours, minutes):
    return ((hours * 60 * 60)+(minutes * 60))
# Main program ends here.
# My code after this.
# print('Your entered hours and minutes being converted into seconds is:- {}'.format(convert(24)))
# The other parameter input should not be compulsory as in the case above.
print('Your entered hours and minutes being converted into seconds is:- {}'.format(convert(24,0)))
print('Your entered hours and minutes being converted into seconds is:- {}'.format(convert(24,1)))
print('Your entered hours and minutes being converted into seconds is:- {}'.format(convert(24,2)))
print('Your entered hours and minutes being converted into seconds is:- {}'.format(convert(1,1)))
print('Your entered hours and minutes being converted into seconds is:- {}'.format(convert(10,10)))
print('Your entered hours and minutes being converted into seconds is:- {}'.format(convert(5,30)))
print('Your entered hours and minutes being converted into seconds is:- {}'.format(convert(1,30)))
# Crossed checked the program is correct.
# Congratulations, Nitkarsh.
# Should make a program which asks user again and again for the input, until the user wants to stop.