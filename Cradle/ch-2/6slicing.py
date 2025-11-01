# accessing parts of string
# str[starting_idx : ending_idx]
# ending idx is not included
# it all starts from 0
str1 = "bebaaahealll"
print(str1[1:5])
print(str1[0])
print(str1[0:5])
print(len(str1))
print(str1[6:12])
print(str1[1:5])
print(str1[1:len(str1)])
# we can always use len(str) for inputting the last index
print(str1[0:len(str1)])
print(str1[0:]) #will print the complete string/ [0:12]
print(str1[:len(str1)])     #[0:len(str1)]
