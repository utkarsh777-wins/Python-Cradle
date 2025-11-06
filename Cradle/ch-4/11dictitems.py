student = {
    "name" : "reo stat",
    "subjects" : {
        "CS" : 99,
        "Maths" : 99,
        "Physics" : 99,
    }
}
print(student.items())
#dict_items([('name', 'reo stat'), ('subjects', {'CS': 99, 'Maths': 99, 'Physics': 99})])
#o/p in form of () which implies tuples, in pairs

print(list(student.items()))
#cursed ya too XD
#[('name', 'reo stat'), ('subjects', {'CS': 99, 'Maths': 99, 'Physics': 99})]
#in the form of a list


"""
cursing it further
tuple manipulation craft

"""
pairs = list(student.items())
print(pairs[0]) 
#calling the 0th index
#o/p: ('name', 'reo stat')
print(pairs[1])
