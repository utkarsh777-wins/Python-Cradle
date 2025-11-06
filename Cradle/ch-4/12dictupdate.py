student = {
    "name" : "reo stat",
    "subjects" : {
        "CS" : 99,
        "Maths" : 99,
        "Physics" : 99,
    }
}

#meth1
student.update({"city" : "delhi"})
print(student)

#meth2
sec_meth = {"city" : "delhi"}
print(student)

"""
{'name': 'reo stat', 'subjects': {'CS': 99, 'Maths': 99, 'Physics': 99}, 'city': 'delhi'}
same output in both cases

"""

