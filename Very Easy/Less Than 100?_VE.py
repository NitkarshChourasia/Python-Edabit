"""
Given two numbers, return true if the sum of both numbers is less than 100.
Otherwise return false.
Examples:-

lessThan100(22, 15) ➞ true
// 22 + 15 = 37

lessThan100(83, 34) ➞ false
// 83 + 34 = 117

lessThan100(3, 77) ➞ true
"""

# Main program starts here.

def lessThanHundred(num1, num2):
    if (num1+num2) < 100:
        return True
    else:
        return False

# Main program ends here.
# Testing my program using various inputs.

print(lessThanHundred(22,15))
print(lessThanHundred(83,34))
print(lessThanHundred(3,77))

# Program works as expected.
# Well done, Nitkarsh Chourasia
# On successful program completion.
# Indeed.
