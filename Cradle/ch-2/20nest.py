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


#let's get our hands on functions
def drive(age):
    if(age >= 18):
        if(age >= 80):
            print("cannot drive")
        else:
            print("can drive")
    else:
        print("cannot drive")

drive(19)
drive(8)
drive(91)
drive(44)
drive(8999900001)

def light(color):
    if(color == "red"):
        return "STOP"
    elif(color == "yellow"):
        return "GET READY"
    elif(color == "green"):
        return "GO"
    else:
        return "Light is broken, kindly be aware of your surroundings and proceed with caution"
    
z = "red"
print(light(z))
print(light("yellow"))
print(light("green"))
print(light("purple"))