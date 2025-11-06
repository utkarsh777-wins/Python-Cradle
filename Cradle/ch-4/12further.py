student = {
    "name" : "reo stat",
    "subjects" : {
        "CS" : 99,
        "Maths" : 99,
        "Physics" : 99,
    }
}

# new_dict = {"city" : "delhi" , "age" : "19"}
# student.update(new_dict)

# print(student)

new_dict = {"name" : "happy", "age" : 16}
student.update(new_dict)

print(student)

"""
{'name': 'happy', 'subjects': {'CS': 99, 'Maths': 99, 'Physics': 99}, 'age': 16}
since duplicate keys ain't allowed in dictionaries
hence the new value replaced the old one
#overwrite

"""