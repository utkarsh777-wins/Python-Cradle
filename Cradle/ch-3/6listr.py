# not supported between instances of 'str' and 'int'
# hence is why these two are done seperately


list = ['a', 'b', 'c', 'z', 'd']
list.sort()
print(list)
list.append('x')
print(list)
list.reverse()
print(list)
list.insert(3, 's')
print(list)