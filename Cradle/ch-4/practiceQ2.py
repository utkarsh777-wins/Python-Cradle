# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as values. 
All_subjects = {}

marks_1 = input()
marks_2 = input()
marks_3 = input()

vk = {
    "CS" : marks_1,
    "PHYSICS" : marks_2,
    "MATHS" : marks_3,
    }

All_subjects.update(vk)

print(All_subjects)
# 