class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

s1 = Student("Deepak", 25)
print(s1.name)  # Output: Deepak
print(s1.age)   # Output: 25

'''
s1 = Student("Deepak", 25)
# Internally becomes:
# Student.__init__(s1, "Deepak", 25)

'''

# Quick Exercise

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def show_details(self):
        print("Account Holder: " + self.account_holder)
        print("Balance: INR " + str(self.balance))


acc1 = BankAccount("Deepak", 5000)
acc1.show_details()
