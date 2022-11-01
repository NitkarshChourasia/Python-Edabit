"""
Luke Skywalker has family and friends. Help him remind them who is who.
Given a string with a name, return the relation of that person to Luke.
Person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid

relation_to_luke("Darth Vader") ➞ "Luke, I am your father."

relation_to_luke("Leia") ➞ "Luke, I am your sister."
"""


# Main program starts here.
# I know there is a more efficient way of doing things, using classes.
# Maybe when I'll learn classes then I can do it.
# Let's start for now.

statement1 = 'Luke, I am your'
def relationAssign(name):
    # name.lower()
    if name.lower() == 'darth vader':
        print(statement1+ ' ' + 'father' + '.')
    elif name.lower() == 'leia':
        print(statement1 + ' ' + 'sister' + '.')
    elif name.lower() == 'han':
        print(statement1 + ' ' + 'brother in law' + '.')
    elif name.lower() == 'r2d2':
        print(statement1 + ' ' + 'droid' + '.')
    else:
        print('Just fuck off from here.')

# Main program ends here.
# My code testing starts from here.
relationAssign('DaRtH VaDER')
relationAssign('lEIA')
relationAssign('HAn')
relationAssign('Hello, kaise ho')
relationAssign('r2d2')
relationAssign('Hi')
relationAssign('Hello, kaise ho')
