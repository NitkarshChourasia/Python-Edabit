# What is expected in a program.
# To create a function that calculates the total number of points.
# Wins gets 3 unit points.
# Draws gets 1 unit points.
# Losses gets 0 unit points.

# Edubit submitted program.
# Main program starts here.
def footballPoints ( Wins, Draws, Losses):
    # Wins = 3 units
    # Draws = 1 units
    # Losses = 0 units
    return ((Wins * 3)+(Draws * 1)+(Losses*0))
# Main program ends here.
# My code after this.
print(footballPoints(4,5,3))
print(footballPoints(2,3,3))
print(footballPoints(3,21,3))
print(footballPoints(30,20,1))
