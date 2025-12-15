class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = Account("12211", "azure16")

print(acc1.acc_no)
print(acc1.acc_pass)
# in this case the security of the account decreases
# which is a bad practice
# hence is why we make and attribute private