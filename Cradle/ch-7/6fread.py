#readline
f = open("Cradle\\ch-7\\demo.txt", "r")

line1 = f.readline()
print(line1)

# --\n exists each time we tap enter
line2 = f.readline()
print(line2)

f.close()
# readlines reads all lines into a lines at once
# readline reads them line by line