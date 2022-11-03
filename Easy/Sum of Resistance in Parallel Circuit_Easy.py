"""
If two or more resistors are connected in parallel, the overall resistance of the circuit reduces. It is possible to calculate the total resistance of a parallel circuit by using this formula:

1/RTotal = 1/R1 + 1/R2 + 1/R3 ...

Create a function that takes a list of parallel resistance values, and calculates the total resistance of the circuit.
Worked Example

parallel_resistance([6, 3, 6]) ➞ 1.5

# 1/RTotal = 1/6 + 1/3 + 1/6
# 1/RTotal = 2/3
# RTotal = 3/2 = 1.5

Examples

parallel_resistance([6, 3]) ➞ 2

parallel_resistance([10, 20, 10]) ➞ 4

parallel_resistance([500, 500, 500]) ➞ 166.6
# Round to the nearest decimal place

Notes

    Note that you should rearrange to return the RTotal, not 1 / RTotal.
    Round to the nearest decimal place.
    All inputs will be valid.
"""

# Main program starts here.
def parallelResistance(list1):
    sum = 0
    rTotal = list1
    # I will have to split it through for loop and then sum it through for loop.
    inverted = (1/rTotal)
    for i in list1:
        # sum = sum + (1/i)
        a = (1/i)
    print(inverted)

# parallelResistance([6,3,6])

# Splitting of lists.
def splitOfLists(lst1):
    n = 0
    countto = len(lst1)
    while(n <= countto):
        print(lst1[n])
        n = n + 1
splitOfLists([1,2,3,4,5,6,7,8,9])
