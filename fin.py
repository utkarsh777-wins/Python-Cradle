# # #create and write to a file 
# # f = open("note.txt", "w")
# # f.write("This is my first note.\n")
# # f.write("learning file handling in python.\n")
# # f.close()

# # #read a file and print that content
# # r = open("note.txt", "r")
# # print(r.read())
# # f.close()

# # # count number of lines in a file
# # c = open("note.txt", "r")
# # lines = c.readlines()
# # print("Total lines", len(lines))
# # c.close()

# # #  count words
# # f = open("note.txt", "r")
# # text = f.read()
# # word = text.split()
# # print("Total count", len(word))
# # f.close()

# # # count character
# # f = open("note.txt", "r")
# # print("No. of Characters:" ,len(f.read()))
# # f.close()

# # # copy content to another file
# # source = open("note.txt", "r")
# # data = source.read()
# # source.close()
# # data_copy = open("data.txt", "w")
# # data_copy.write(data)
# # data_copy.close()
# # #append text
# # f = open("note.txt", "a")
# # f.write("\napppppppppppennndddddddd")
# # f.close()

# #read first 10 characters
# f = open("note.txt", "r")
# print(f.read(10))
# f.close()

# #count occurences of a word
# f = open("note.txt", "r")
# text = f.read()
# count = text.count("file")
# print("Occurence", count)
# f.close()

# # a = ["apple", "orange"]
# # f = open("fruits.txt", "w")
# # for item in a:
# #     f.write(item + "\n")
# # f.close()

# f = open("shii.txt", "w")
# for item in f:
#     f.write(item + "\n")
# f.close()

# f = open("fruits.txt", "r")
# line = f.readlines()
# f.close()
# for i in enumerate(line, start = 1):
#     a = []
#     a.append(i)
f = open("fruits.txt", "r")
f1 = f.read()
print(f1)
print(type(f1))