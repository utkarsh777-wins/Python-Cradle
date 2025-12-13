# with syntax
# f or file
'''
with open("auto.txt", "a") as f:
    data = f.read()

    f is an alias
    with automatically closes the file for us 

'''
with open("auto.txt", "r") as f:
    data = f.read()
    print(data)

with open("auto.txt", "w") as f:
    f.write("new data")
    #it'll output the old data and overwrite the new data in