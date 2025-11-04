# WAP to check if a list contains a palindromem of elements.
# palindromes- smae from front and back, eg "maam" "racecar" 
list1 = [1, 2, 2]       #[1, 2, 1]
list2 = ["m", "a", "a", "m"]

copy_list1 = list1.copy()
copy_list1.reverse()
copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("Palindrome")
else:
    print("Not Palindrome")


if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")
copy_list2 = list2.copy()
