#figure out a way to store 9 & 9.0 as seperate values in the set.
#you can take help of built in data types
sol_1 = {9, "9.0"}
print(sol_1)


set_a = set()
nines = (9, 9.0)    #tuples
set_a.add(nines)

print(set_a)

sol_3 = {
    ("float", 9.0),
    ("int", 9),
}
print(sol_3)