student = {
    "name" : "reo stat",
    "subjects" : {
        "CS" : 99,
        "Maths" : 99,
        "Physics" : 99,
    }
}

print(student.values())
#o/p : dict_values(['reo stat', {'CS': 99, 'Maths': 99, 'Physics': 99}])  
#values include all the input given in the value section

#casting some craft into this
print(list(student.values()))   
#cursed ya XD to be a list
#['reo stat', {'CS': 99, 'Maths': 99, 'Physics': 99}]
#dictionary within a list is a bit intriguing