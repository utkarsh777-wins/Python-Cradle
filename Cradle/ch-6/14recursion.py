# When a function calls itself repeatedly.
# loops-recrursion are interrealted
#print n to 1 backwards
def show(n):
    if(n ==0):  #base case
        return
    print(n)
    show(n-1)