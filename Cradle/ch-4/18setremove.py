collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

collection.remove(1)
# collection.remove(7)
#o/p: KeyError: 7, in case of irrelevent value
print(collection)
