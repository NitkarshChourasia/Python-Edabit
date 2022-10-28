# def calculate_exponent(num, exp):
#     i = 1
#     while ( i <= exp):
#         output1 = num*num*(i)
#         print(output1)
#         print(i)
#         i = i + 1
#         while (i <= exp):
    # while (i <= exp):
    #     for j in range(exp):
    #         b = exp * exp
    #         print(j)
    #     i = i+1

# calculate_exponent(2, 5)
# exp = 5
# for j in range(1,exp+1):
#     b = exp*exp
#     print(exp)
# print(b)
# def best(hey, how):
#     a = hey ** how
#     print(a)
# best(2,5)
######## Main program starts here #############
def calculate_exponent(num, exp):
    return num ** exp
a = calculate_exponent(2,5)
print(a)
######## Main program ends here ###############
# Doesn't return statement print something? No The return statement does not print out the value
# it returns when the function is called.
# so to print we do something like the above.
def hello():
    return 2*2
hello()