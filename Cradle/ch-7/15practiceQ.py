# create a new file "practice.txt" using python. Add the following data in it:
# f = open("practice.txt", "w")
# f.write("Hi everyone \n")
# f.close()

# f = open("practice.txt", "a")
# data = f.write("we are learning File I/O \n")
# f.write("using Java. \n")
# f.write("I like programming in Java")
with open("practice.txt", "w") as file:
    file.write("Hi everyon\nwe are learning File I/O\n")
    file.write("using Java.\nI like programming in Java")