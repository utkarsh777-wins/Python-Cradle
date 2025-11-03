"""
Grade students based upon

marks >= 90, grade="A"
90 > marks >= 80, grade="B"
80 > marks >= 70, grade="C"
70 > marks >= 60, grade="D"

"""
marks = int(input("Enter Marks: "))

if(marks >= 90):
    grade = "A"
    # print("Grade A")
elif(marks < 90 and marks >= 80):
    grade = "B"
    # print("Grade B")
elif(marks < 80 and marks >= 70):
    grade = "C"
    # print("Grade C")
# elif(marks > 70):
#     print("Grade D")
else:
    grade = "D"
    # print("Grade D")
print("Grade of the student -->", grade)
