# list slicing
# ending index is not included

marks = [10, 40, 56, 78, 99]
print(marks[1:4])
print(marks[:4])     #will exclude ending index
print(marks[0:])    #will include all the elements

# negative indexing
print(marks[-3:-1])
print(marks[:-1])
print(len(marks))       #gauge the number of elements
print(marks[-5:])       #print em all