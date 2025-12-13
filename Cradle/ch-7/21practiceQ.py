# From  a file containing numbers seperated by comma, print the count of even numbers.
# f.write() is designed to work with strings
count = 0
with open("prac.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    print(nums)
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

    print(count)



    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         # print(num)
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]