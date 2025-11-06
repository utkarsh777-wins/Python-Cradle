# typecasting in lists
student = {
    "name" : "reo stat",
    "subjects" : {
        "CS" : 99,
        "Maths" : 99,
        "Physics" : 99,
    }
}


print(list(student.keys()))

#length of the dictionary
print(len(student))
print(len(list(student.keys())))    #typecast