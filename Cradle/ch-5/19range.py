"""
range function returns a sequence of numbebrs, starting
from 0 by defaault, and increments by 1(by default), and stops 
before a specified number

range(star?, stop, step?)
starting and step value are optional
but stopping values is mandatory

"""
for el in range(5): #stoppinng condition
    print(el)

print("END") #at the end of the loop

for el in range(1, 5):
    print(el)

print("END")


for el in range(1, 5, 2):
    print(el)

print("END")

"""
0
1
2
3
4
END
1
2
3
4
END
1
3
END

"""