#wap to find the sum of first n numbers (using while) 1+2+3+4
# n = int(input("ENTER:"))

# sum = 0
# for i in range(1, n+1):
#     sum += i

# print("total sum:", sum)
n = int(input("ENTER:"))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("total sum", sum)