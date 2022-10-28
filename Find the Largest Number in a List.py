def findlargestNum():
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
findlargestNum()

# To test whether a function can run it's own inherited functions?


# edabit submitted solution:
def findLargestNum(nums):
	return(max(nums))