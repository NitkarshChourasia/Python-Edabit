"""
Create a function that takes an angle in radians and
returns the corresponding angle in degrees rounded to one decimal place.
Examples:
    radians_to_degrees(1) ➞ 57.3
Notes:
    The number π can be loaded from the math module with from math import pi.
"""
# Main program starts here.
from math import pi

def radToDeg(radian):
    main = radian * (180/pi)