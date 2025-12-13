f = open("Cradle\\ch-7\\demo.txt", "r")   
# f = open("Cradle\ch-7\demo.txt", "rt")   #t is implicit
data = f.read()
print(data)
print(type(data))
f.close()
#must close your files
#leaving your files at open involves the risk of unauthorised access.

#passing parameters in read
f = open("Cradle\\ch-7\\demo.txt", "r")

data = f.read(7)
print(data)

f.close()
