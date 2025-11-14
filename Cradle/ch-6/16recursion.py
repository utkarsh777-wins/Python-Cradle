# returns n!    --recurrence relation
def fact(n):
    if(n == 0 or n == 1):   #base case
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))

#fact4=>fact3*4=>fact2*3*4=>fact1*2*3*4
#layer by layer this process works backwards