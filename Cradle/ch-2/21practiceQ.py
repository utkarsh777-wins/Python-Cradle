# WAP to check if a number entered by the user is odd or even
user = int(input("User-sama, enter number: "))

if(user % 2 == 0):  #even numbers are multiples of 2
    print("EVEN")
else:
    print("ODD")

# WAP to find the greatest of 3 numbers entered by the user
s = int(input("Enter first number: "))
t = int(input("Enter second number: "))
u = int(input("Enter third number: "))

if(s >= t and t >=u):
    print("FIRST NUMBER IS LARGEST", s)
elif(t >= u):      #if already checked the above statement
    print("SECOND NUMBER IS LARGEST", t)
else:
    print("THIRD NUMBER IS LARGEST", u)

"""
if(a > b and a > c):
    print("a is bigg")
elif(b > a and b > c):
    print("b is bigg")
# elif()
else:
    print("c is bigg")

"""

# WAP to check if a number is a multiple of 7 or not
multiple = int(input("Enter your number: "))

if(multiple % 7 == 0):
    print("Yesshh")
else:
    print("Noii")

# WAP to check the largest of 4 numbers
a = int(input("Enter Your 1st Number: "))
b = int(input("Enter Your 2nd Number: "))
c = int(input("Enter Your 3rd Number: "))
d = int(input("Enter Your 4th Number: "))

if(a > b and b > c and c > d):          #checked for a 
    print("a is big")
elif(b > c and c > d):
    print("b is big")                   #checked for b
elif(c > d):
    print("c is big")                   #checked for c
else:
    print("D is big")