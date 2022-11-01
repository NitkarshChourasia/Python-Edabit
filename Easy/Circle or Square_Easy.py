"""
Given the radius of a circle and the area of a square,
return True if the circumference of the circle is greater than the square's perimeter and
False if the square's perimeter is greater than the circumference of the circle.
# Examples:-
    circle_or_square(16, 625) ➞ True
    circle_or_square(5, 100) ➞ False

Notes:-
        You can use Pi to 2 decimal places (3.14).
    Circumference of a circle equals 2 * Pi * radius.
    To find the perimeter of a square using its area,
    find the square root of area (to get side length) and multiply that by 4.
"""

# Main program starts here.

from math import pi
from math import sqrt


def cirSqTrueFalse(radius, area):
   # modpi = round(pi, 2)
   # print(modpi)

    periOfSq = 4*(sqrt(area))
    circumOfCircle = 2 * pi * radius
    if periOfSq < circumOfCircle:
        return True
    else:
        return False

# Main program ends here.
# My code test after this.

print(cirSqTrueFalse(16, 625))
print(cirSqTrueFalse(5, 100))
print(cirSqTrueFalse(8, 144))

# I will check all this code, later, with respect to their outputs, and functions.