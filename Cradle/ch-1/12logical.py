# logical operators
# works based upon boolean values
# not

print(not False)
print(not True)

a = 50
b = 30
print(not (a > b))
# opposite value of actual boolean values

# and
# works upon various operands
value1 = True
value2 = True
print("and operator:", value1 and value2)
value1 = True
value2 = False
print("and operator:", value1 and value2)
# true only if both the value are true

#or
value1 = True
value2 = True
print("OR operator:", value1 or value2)
#returns true if either of the values is true
#returns false if both the values false
print((a == b) or (a > b))
# a==b is False
# a>b is True
#True
