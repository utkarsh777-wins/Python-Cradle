t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Pick a number from the tuple:"))

i = 0   #initialization
while i < len(t):
    if(t[i] == x):
        print("FOUND at idx", i)
    i += 1

#finding
t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = int(input("Pick a number from the tuple:"))

idx = 0   #initialization
while idx < len(t):
    if(t[idx] == x):
        print("FOUND at idx", idx)
    else:
        print("finding...")
    
    idx += 1

    """
pick a number from the tuple:36
finding...
finding...
finding...
finding...
finding...
FOUND at idx 5
finding...
finding...
finding...
finding...
FOUND at idx 10

    """