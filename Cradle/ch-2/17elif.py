# else-if
# 

age = 0

if(age >= 18):
    print("Can vote & Apply for license")
elif(age > 16 and age < 18):
    print("Cannot fly")
    # the next line of code gets ignored, once match is found
elif(age == 0):
    print("Null vector")
# we can write multiple if and elif statements 
# but there needs to be at least one if before we start using elif
# elif will only check when if conditon is false


print("End of code")

num = 5

if(num > 2):
    print("greater than 2")
elif(num > 3):
    print("greater than 3")