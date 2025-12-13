# WAP that replaces all occurrences of java with python in above list
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
new_data = data.replace("everyon", "everyone")
print(new_data)
#works since data is a string

with open("practice.txt", "w") as f:
    f.write(new_data)
