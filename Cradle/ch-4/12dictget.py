student = {
    "name" : "reo stat",
    "subjects" : {
        "CS" : 99,
        "Maths" : 99,
        "Physics" : 99,
    }
}

print(student["name"])
print(student.get("name"))

#imp
# print(student["name2"])
#o/p: KeyError: 'name2'
#code after the error won't run, so errors are imp
print(student.get("name2"))
#o/p: None