def check_for_word():
   with open("practice.txt", "r") as file:
     data = file.read()
     if(data.find(word) != -1):
        print("Found")
     else:
        print("Does not exist")

word = input()
check_for_word()