#using for print the list heh = [11, 44, 99, 66, 88, 66, 988, 3000]
heh = [11, 44, 99, 66, 88, 66, 988, 3000]

for val in heh:
    print(val)

# search for a number x in this tuple using for
search = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 64) #liner search --searching in a single line
x = int(input("Enter your number: "))

idx = 0
for num in search:
    if(num == x):
        print("X was here", idx)
        # break will quit the loop onc ethe value is found
    idx += 1    #added to track the index
# X was here 7
# X was here 10