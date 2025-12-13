# # point starts overwritting from the beginning of the file
# f = open("auto.txt", "w+")
# # f.write("acz")
# print(f.read())
# f.write("acz")
# # and the file got wiped clean
# # won't print anything in w+ mode
# f.close()
f = open("auto.txt", "a+")
print(f.read())
f.write("aczzz")
f.close()
#no overwritting just append
