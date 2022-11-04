"""
Create a function that validates whether three given integers form a Pythagorean triplet.
The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.
Examples

is_triplet(3, 4, 5) ➞ True
# 3² + 4² = 25
# 5² = 25

is_triplet(13, 5, 12) ➞ True
# 5² + 12² = 169
# 13² = 169

is_triplet(1, 2, 3) ➞ False
# 1² + 2² = 5
# 3² = 9

Notes

Numbers may not be given in a sorted order.
"""
# Main program starts here.

def pyTripletCheck(num1, num2, num3):
    list1 = [num1, num2, num3]
    list1.sort()
    if ((list1[0] ** 2) + (list1[1]**2)) == (list1[2]**2):
        return True
    else:
        return False

# My program input test.

print(pyTripletCheck(3,5,4)) # Should be true.

print(pyTripletCheck(12,5,13)) # Should be true.

print(pyTripletCheck(1,5,3)) # Should be false.

print(pyTripletCheck(3,5,4)) # Should be true.

print(pyTripletCheck(13,5,12)) # Should be true.

# Indeed the program built is perfect.
# Congratulations, Nitkarsh Chourasia.
# On successful creation of a good program.
# Well done, indeed.