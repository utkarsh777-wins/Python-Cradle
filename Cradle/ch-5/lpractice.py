# Take an integer num as input from the user. Write a code to find the sum of all even numbers from 1 to num using a while construct, print the result to the console as shown in the example.

num = int(input())

count = 1
sum = 0

while count <= num:
    if count % 2 == 0:
        sum += count
    count += 1
print(sum)