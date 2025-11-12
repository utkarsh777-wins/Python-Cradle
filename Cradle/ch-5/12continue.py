# #Continue
# #terminates execution in the current iteration & continues execution of the loop with the next iteration.
# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1  #skipping this iteration
#         continue    #skip
#     print(i)
#     i += 1

# #printing odd numbers
# i = 1
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1
"""

1
3
5
7
9

"""
#printing even numbers
i = 1
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1
"""
2
4
6
8
10

"""