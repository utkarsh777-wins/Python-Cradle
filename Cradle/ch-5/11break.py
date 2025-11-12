#break
#loop will break when break is used
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break   #breaks the loop at 3
    i += 1

print("End of LOOP")

t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)

x = int(input("Pick a number from the tuple:"))

idx = 0   #initialization
while idx < len(t):
    if(t[idx] == x):
        print("FOUND at idx", idx)
        break
    else:
        print("finding...")
    
    idx += 1
    #no more finding after break
print("End of LOOP")