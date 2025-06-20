'''
What is Encapsulation?
Encapsulation means binding data (variables) and methods that operate on the data into one unit (class) — and restricting direct access to some of the class's components.

In Python, encapsulation is achieved using access modifiers.'''

'''
 Python Access Modifiers:
Python doesn't have true private/protected like Java/C++, but we simulate it using naming conventions:

Access Type	Syntax Example	Meaning
Public	self.name	Accessible from anywhere
Protected	self._name	Convention: "internal use only"
Private	self.__name	Name mangled → _ClassName__name'''


class Employee:
    def __init__(self, name, salary):
        self.name = name            # public
        self._department = "Sales"  # protected (by convention)
        self.__salary = salary      # private

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self._department}")
        print(f"Salary: {self.__salary}")  # Allowed here

e1 = Employee("Deepak", 50000)
e1.show_info()

# print(e1.name)         # ✅ Accessible
# print(e1._department)  # ⚠️ Technically accessible, but not recommended
# print(e1.__salary)     # ❌ Error: AttributeError

'''
 How to Access Private Variables (If Needed):
Python does name mangling:

print(e1._Employee__salary)  # ✅ This works
But it’s discouraged unless you're debugging/testing.

'''

'''
 Why Encapsulation?
- To hide internal implementation details.

- To protect sensitive data from being modified accidentally.

- To give access only via methods (getters/setters).

'''


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary >= 30000:
            self.__salary = new_salary
        else:
            print("Salary too low")

e = Employee("Deepak", 50000)
print(e.get_salary())
e.set_salary(25000)   # Won't change
print(e.get_salary())


'''
Summary:
Modifier	Usage	Convention	Access From Outside?
Public	self.name	General	✅ Yes
Protected	self._name	Internal use only	⚠️ Yes (not enforced)
Private	self.__name	Sensitive data	❌ No (name mangling)

'''

'''

🔒 Mini Task: Create a Secure Bank Account Class
📘 Class: BankAccount
✅ Requirements:
Private Attributes:

__account_holder

__balance

Constructor: Takes account_holder and initial_balance

If initial_balance is less than 1000, set balance to 1000 (minimum).

Getter Methods:

get_account_holder() → returns the account holder's name

get_balance() → returns current balance

Setter Method:

set_balance(amount) → only updates if amount >= 1000, else print "Minimum balance must be ₹1000"

Method:

show_account() → displays account holder and balance

🔍 Example Usage:
acc = BankAccount("Deepak", 500)  # balance should be set to 1000
acc.show_account()

acc.set_balance(800)  # should print warning
acc.set_balance(5000)

print("Balance via getter:", acc.get_balance())
🔧 Try writing this class now — focus on using __ for private attributes and clean getter/setter logic.
Once you paste your code, I’ll review it before we proceed to Inheritance in Python.


'''



class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.__account_holder = account_holder
        if initial_balance<1000:
            self.__balance = 1000
        else:
            self.__balance = initial_balance

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance
    def set_balance(self, new_balance):
        if new_balance < 1000:
            print("Minimum balance must be INR 1000")
        else:
            self.__balance = new_balance

    def show_account(self):
        print(f"Account holder: {self.__account_holder} ")
        print(f"Balance : {self.__balance}")

print("\nExercise\n-----------------------------------\n")
acc = BankAccount("Deepak", 500)  # balance should be set to 1000
acc.show_account()

acc.set_balance(800)  # should print warning
acc.set_balance(5000)

print("Balance via getter:", acc.get_balance())

