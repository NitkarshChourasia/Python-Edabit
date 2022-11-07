"""
Create a function that takes two arguments.
Both arguments are integers, a and b.
Return True if one of them is 10 or if their sum is 10.
Examples:

makes10(9, 10) ➞ True

makes10(9, 9) ➞ False

makes10(1, 9) ➞ True

Notes

Don't forget to return the result.
"""

# Main program starts here.

def makes10(num1, num2):
    if (num1 + num2 == 10) or num1 == 10 or num2 == 10:
        return True
    else:
        return False
# Main program ends here.

# Testing my program after this.
print(makes10(9,10))
print(makes10(9,9))
print(makes10(1,9))

# Code executed perfectly.
# Well done, Nitkarsh Chourasia.
# Congratulations on successful code completion.
# Indeed.