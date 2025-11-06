#only values can be stored in sets, unlike dictionaries
collection = {1, 2, 3, 4}

print(collection)
print(type(collection))

collection2 = {5, 6, 6, 6, "hello", "world", "world"}

print(collection2)
print(len(collection2)) #total number of items
#len will also ignore duplicate values
#o/p: 4

#o/p: {'world', 'hello', 5, 6}
#duplicate values got ignored
#and output is always unordered
