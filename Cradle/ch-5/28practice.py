#wap to find the factorial of first n numbers
#1*2*3*4*5
n = int(input("ENTER NUMBER:"))
fact = 1 #initalizing with 1 since *
i = 1
while i <= n:
    fact *= i
    i += 1

print("factorial of number =", fact)

n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print("factorial = ", fact)