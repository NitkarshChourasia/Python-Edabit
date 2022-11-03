"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multi5and3():
    upprange = 1000 + 1
    # i = 0
    sum = 0
    for i in (range(0,upprange, 3)):
        # sum = sum + i
        # print(sum[-1])
        # i = i + i
        # print(i)
        arr = []
        a =i
        arr.append(a)
        sum = arr + list(sum)
        # arr
        # i = i + 1
    # while(b <= 1000):
    #         print(b)

# multi5and3()

def multi3and5():
    arr = []
    sum = 0
    for i in range(0, 1000+1, 3):
        # print(i)
        arr.append(i)
    print(arr)
        # for sum1 in arr:
        #     sum = sum + sum1
        #     print(sum)
        # for a in i:
        #     print(a)
    # for j in range(0, 1000+1, 5):
    #     print(j)
multi3and5()

# to find the sum a for loop will be used.
# for i in arr: # array given
# sum = i + sum # like this thing (the logic in it) I have to understand clearly.j

def tri():
    a = []
    for i in range(5):
        # a = []
        a.append(i)
        print(a)
tri()

def tristar():
