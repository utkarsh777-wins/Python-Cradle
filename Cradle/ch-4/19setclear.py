collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("hungryy")
collection.add((1, 2, 3))

print(len(collection)) #4

collection.clear()
print(len(collection)) #0