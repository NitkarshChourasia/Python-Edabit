""""# Notes :-
# Assume all input is in lower case and at least two characters long.
Write a function that stutters a word as if someone is struggling to read it.
The first two letters are repeated twice with an ellipsis ... and space after each,
and then the word is pronounced with a question mark ?.
Example:
    stutter("incredible") ➞ "in... in... incredible?"
"""
# Main program starts here.
def stutter(word):
    return word[:2] + "... " + word[:2] +"... " + word + "?"
# Incase of return I can use print also but it is more of a good practice I think to do so...
# To type return, Why? Because it is not everytime you want to print something... right?
# Main program ends here.
# My test of code after this.

print(stutter("incredible"))
stutter("incredible")  # It doesn't return anything...unless function is used within print function....
print(stutter("enthusiastic"))
print(stutter("outstanding"))

# My test of codes ends here.