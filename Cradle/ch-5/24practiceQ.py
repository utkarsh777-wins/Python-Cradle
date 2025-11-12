# using for and range
#print numbers from 1 to 100
for i in range(1, 101): #range(start, stop)
    print(i)
print("END")

#print numbers from 100 to 1
for r in range(100, 0, -1): #range(start, stop, step)
    print(r)    #step size is neagtive

#multiplication table of a number n
n = int(input("ENTER:"))

for num in range(1, 11): #(start, stop)
    print(n*num)