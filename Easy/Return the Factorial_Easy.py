"""
Create a function that takes an integer and returns the factorial of that integer.
That is, the integer multiplied by all positive lower integers.
Examples

factorial(3) ➞ 6

factorial(5) ➞ 120

factorial(13) ➞ 6227020800

Notes

Assume all inputs are greater than or equal to 0.
"""
def factorial1(num2):
    # global fact
    fact = 1
    for i in range(1,num2 + 1):
    # i = 1
    # while (i <= num2):
        fact = i * fact # Finally used this Assignment Operators.
        i += 1
    print(num2)
    return (fact) # Okay when return statement is not used... It outputs none, so using that at the end avoids that output none thing...
    # print(fact) # Testing whether after using return statement does it works or not...? and it doesn't work nor outputs any error.
    # return fact
print(factorial1(3))
print(factorial1(5))
print(factorial1(13))
print(factorial1(20))
# print(fact)
# So the variables used inside the function is not valid outside the function, so it is local, I see.
# Let's make it global and see whether it prints anything or not.
# Let's test.
# print(fact) # so after making it global it does works outside the function...
# Congratulations on learning something new... # Well done, Nitkarsh Chourasia.
# Main program ends here.
# Today was good.
# Congratulations, Nitkarsh Chourasia on building something new...
# Now, let's move on to the next topic, so.
