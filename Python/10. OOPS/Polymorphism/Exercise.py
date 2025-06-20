'''
"Polymorphic Payment System"
🎯 Task:
Design a system where users can pay using different methods (like UPI, CreditCard, or Cash). Each class must implement a make_payment(amount) method.

Then, create a function process_payment(payment_method, amount) which accepts any object that has a make_payment() method — this is where duck typing comes in!

🧩 Requirements:
Define a base class PaymentMethod with a method make_payment(amount)

Create three subclasses: UPI, CreditCard, Cash

Each subclass must override the make_payment method with its own logic/message

The process_payment function must call .make_payment(amount) without caring which class is passed

🔖 Example Output:

process_payment(UPI(), 500)
# Output: Paid ₹500 via UPI.

process_payment(CreditCard(), 1000)
# Output: Paid ₹1000 using Credit Card.

process_payment(Cash(), 300)
# Output: Paid ₹300 in Cash.
✍️ Your Turn:
Write the complete code based on the above specs.
Once done, share it here — and I’ll review and suggest any improvements.'''


class  PaymentMethood:
     def make_payment(self, amount):
          print(f"Amount Paid {amount}")

class UPI(PaymentMethood):
     def make_payment(self, amount):
          print(f"Payment Done using UPI {amount}")

class CreditCard(PaymentMethood):
     def make_payment(self, amount):
          print(f"Payment Done using CreditCard: {amount}")

class Cash(PaymentMethood):
     def make_payment(self, amount):
          print(f"Payment Done using Case : {amount}")

def process_payment(method, amount):
     return method.make_payment(amount)

process_payment(UPI(), 500)
process_payment(CreditCard(), 1000)
process_payment(Cash(), 300)


# Challenge 2
'''
 Challenge: "Smart Report Generator"
🎯 Goal:
You're building a system to generate reports for different data types: employees, products, and customers. Each type will have its own way of generating reports — but the report system shouldn't care what type of object it is.

✅ Requirements:
Define 3 classes: Employee, Product, Customer

Each class must have a generate_report() method (with different logic):

Employee → Show name, designation, salary

Product → Show product name, price, stock

Customer → Show name, email, membership level

Create a function print_report(obj) that takes any object and calls obj.generate_report() using duck typing.

Add some formatting to distinguish reports (e.g., headers, lines)

🔖 Sample Output:
makefile
Copy
Edit
===== Employee Report =====
Name: Deepak
Role: Developer
Salary: ₹80000

===== Product Report =====
Product: Laptop
Price: ₹75000
Stock: 15 units

===== Customer Report =====
Customer: Rahul
Email: rahul@example.com
Membership: Gold
🧪 Bonus (Optional Challenge):
Add a common interface class like Reportable using abc.ABC to enforce generate_report() in all subclasses.

'''


from abc import ABC, abstractmethod

# Abstract base class to enforce generate_report()
class Reportable(ABC):
    @abstractmethod
    def generate_report(self):
        pass

# ===== Employee Class =====
class Employee(Reportable):
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def generate_report(self):
        print("===== Employee Report =====")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Salary: INR{self.salary}\n")

# ===== Product Class =====
class Product(Reportable):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def generate_report(self):
        print("===== Product Report =====")
        print(f"Product: {self.name}")
        print(f"Price: INR{self.price}")
        print(f"Stock: {self.stock} units\n")

# ===== Customer Class =====
class Customer(Reportable):
    def __init__(self, name, email, membership):
        self.name = name
        self.email = email
        self.membership = membership

    def generate_report(self):
        print("===== Customer Report =====")
        print(f"Customer: {self.name}")
        print(f"Email: {self.email}")
        print(f"Membership: {self.membership}\n")

# ===== Duck Typing in Action =====
def print_report(obj: Reportable):
    obj.generate_report()

# Test runs
e = Employee("Deepak", "Developer", 80000)
p = Product("Laptop", 75000, 15)
c = Customer("Rahul", "rahul@example.com", "Gold")

print_report(e)
print_report(p)
print_report(c)
