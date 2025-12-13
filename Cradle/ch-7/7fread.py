
f = open("Cradle\\ch-7\\demo.txt", "r")

data = f.read()
print(data)

#since we've already read the file,
#readlines will give empty output as theres simply nothing else to read

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

