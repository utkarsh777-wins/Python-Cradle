# nested dictionary

student = {
    "name" : "reo stat",
    "subjects" : {
        "CS" : 99,
        "Maths" : 99,
        "Physics" : 99,
    }
}

print(student)
print(student["subjects"]["CS"])
#nesteed printing (o/P: 99 --value for that key)
