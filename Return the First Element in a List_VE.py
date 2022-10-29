# Edabit submitted solution.
# Main program starts here.
def returnFirstValue(intlist1):
# I think there are multiple ways to input values.
# First: by creating a list separately.
# Second: by creating a list while printing.
# Let's see both the methods.
# In future, do make some more improvements as needed.
    return intlist1[0] # Is this method right? Yeah it is working I guess.
# Main program ends here.
# My code after this.
intlist1 = [432,2342,23424,131,123,2455,999999]
intlist1.sort(reverse=True)
print('Printing the first int by sorting them first:\n{}'.format(returnFirstValue(intlist1)))
print('Printing by inputting the list in print function itself:\n{}'.format(returnFirstValue([11,3,52,432,234,23,3])))