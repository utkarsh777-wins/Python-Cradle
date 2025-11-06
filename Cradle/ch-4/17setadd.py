collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("hungryy")
collection.add((1, 2, 3))

"""
collection.add([1, 2, 3])
TypeError: unhashable type: 'list'
hashing: overview --soecific algo/method in which original value is converted
in this case the hash value of set will change 
which will bug th eimplementation of set

hence, unhashable - dict, list, set

"""

print(collection)

