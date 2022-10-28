def findlargestNummine():
    arrsize = int(input('Please input array size:\n'))
    i = 1
    list1 = []
    while (i <= arrsize):
        listinput1 = int(input('Please input elements:\n'))
        # list1 = []
        # What I was doing was that I was declaring it empty again and again,
        # and then appending again and again that's why it shown only one character.

        list1.append(listinput1)
        i = i + 1
    print(list1)
    print("Largest number among it is: {}".format(max(list1)))
    """Another way to find the largest number in the list is:-
        list1.sort()
        print(list1[-1})
    """
    list1.sort()
    print('Sort function way to find the largest number in the list: {}'.format(list1[-1]))
# findlargestNummine()

# To test whether a function can run it's own inherited functions?

######### Main Program starts here. ##############
# edabit submitted solution:
def findLargestNum(nums):
	return(max(nums))

######## Main Program ends here. ##################
# Program lines after this were not submitted to the edabit.
# It is for the user to print the outputs, for myself I mean.
b = findLargestNum([5,64,5646,564])
print(b)
# a = findlargestNummine()
# print(a)