# #A function once defined can be used again and again, limitless number of times
# #unlike other codes that need to be updated 
# a = 5
# b = 10

# sum = a + b
# print(sum)



# #more lines of code

# a = 2
# b = 10
# sum = a + b
# print(sum)

# #more lines of code

# c = 21
# b = 10
# sum = a + b
# print(sum)
#redundant code - same sort of code repeated again and again
#so we define a function in these cases 
# fn parameters()
def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(99, 369)

calc_sum(1, 9)

calc_sum(11, 110)
#we can keep calling the function with parameters like this