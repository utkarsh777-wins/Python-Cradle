#recursive function
def show(n):
    if(n == 0):
        return 
    print(n)
    show(n-1)

show(5)  #5, 4, 3, 2, 1
print("END")
show(3)

# call stack--  --stack of function calls
#stacks move backwards once te task is completed while deleting the stack layers present on its way back