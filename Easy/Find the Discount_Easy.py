"""
Create a function that takes two arguments:
the original price and the discount percentage as integers and returns the final price after the discount.
Examples:
    dis(1500, 50) ➞ 750
# Notes:
    Your answer should be rounded to two decimal places.
"""
# Main program starts here.
def discountProgram(price, discPerc):
    main = price - (price * (discPerc/100))
    return ("{0:.2f}".format(main)) # This one is good, Why? Because it shows 00 zeroes all the time...
    # return (round(main,2)) # This one shows not all the zeroes all the time, but when needed then it shows.
# Should learn to apply constraints too.

# Main program ends here.
# My code test here.
print(discountProgram(100,50))
print(discountProgram(100,75))
print(discountProgram(1500, 50))
print(discountProgram(89, 20))
print(discountProgram(100,75))

# Now it is perfect, showing the final price which was about to be paid upfront.
