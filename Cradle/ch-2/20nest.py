#Nesting
"""
conditional statement within another conditional statement


"""
age = 99

if(age >= 18):
    if(age >= 80):          #nesting
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

