#input casting in python
int("5")
val = int(input("Enter some value: "))
print(type(val), val)

#converting input to int andfloat through casting, of there's a limit to this as well..

val = float(input("Enter some value: "))
print(type(val), val)

name = input("enter name: ")
age = input("enter age: ")
marks = input("enter marks: ")

print("Welcome", name)
print("Age =", age)
print("Marks =", marks)

#casting --spell -internally present but no change externally

name = input("enter name: ")
age = int(input("enter age: "))
marks = float(input("enter marks: "))

print("Welcome", name)
print("Age =", age)
print("Marks =", marks)
