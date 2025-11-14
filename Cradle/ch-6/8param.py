#default parameters
#Assinging a default value to paramater, which is used when no arguement is passed.
# def cal_prod(a, b):
#     print(a * b)
#     return a * b

# cal_prod()
# cal_prod() missing 2 required positional arguments: 'a' and 'b'
def cal_prod(a=4, b=2):
    print(a * b)
    return a * b

cal_prod()

def cal_mul(a, b=3):
    print(a * b)
    return a * b

cal_mul(9)

# def cal_mul(a=6, b):
#     print(a * b)
#     return a * b

# cal_mul(9)
# parameter without a default follows parameter with a default