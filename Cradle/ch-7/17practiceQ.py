#search if the word "learning" exists in the file or not
word = "learning"
# word = "xlearning"  Does not exist
with open("practice.txt", "r") as file:
    data = file.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Does not exist")
