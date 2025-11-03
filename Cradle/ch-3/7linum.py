list = [2, 1, 3]
list.append(4)  #adds one element at the end 
print(list)

list.sort() #sorts in ascending order
# print(list.sort())      #none-won't return any output
print(list)
list.sort( reverse=True )  #sorts in descending order
print(list)
list.reverse()
print(list)  #reverse list
# list.insert( idx,el )
list.insert( 1,4 )
print(list)
list.remove(3)
print(list)
list.pop(3)
print(list)
