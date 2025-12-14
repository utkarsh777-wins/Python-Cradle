# create and account class with 2 attributes - balance and account no
# create methods for debit, credit & printing the balance
class Account:
    def __innit__(self, number, balance):
        self.acc = number
        self.bal = balance

    def debit(self):
        account_number = self.acc
        debit = int(input())
        print(f"{debit} amount has been debited to {account_number}")
        print(f"Account Balance:{self.bal + debit}")

    def credit(self):
        account_number = self.acc
        credit = int(input())
        print(f"{credit} amount has been credited from {account_number}")
        print(f"Account Balance:{self.balance - credit}")

    def balance(self):
        print(f"Current Balance:{self.bal} of your account {self.acc}")


c1 = Account(121, 60000)
# Account() takes no arguments
# fix this