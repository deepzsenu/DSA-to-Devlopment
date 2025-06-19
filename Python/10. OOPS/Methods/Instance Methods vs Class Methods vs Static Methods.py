'''
Instance Methods — 👤 Belong to the Object
📌 Definition:
The default method type inside a class.

First parameter is always self (the current object).

Can access instance variables and class variables.'''

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

p = Person("Deepak")
p.greet()  # Output: Hello, my name is Deepak


'''
2. Class Methods — 🏛️ Belong to the Class, Not Object
📌 Definition:
Use the @classmethod decorator.

First parameter is cls (refers to the class itself, not the instance).

Can access or modify class variables.

Cannot access instance variables directly.'''
class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Student.change_school("XYZ School")
print(Student.school)  # Output: XYZ School


'''
3. Static Methods — ⚙️ Utility Functions Inside a Class
📌 Definition:
Use the @staticmethod decorator.

No self or cls parameter.

Cannot access instance or class variables.

Behaves like a regular function, but lives inside the class for logical grouping.'''
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 3))  # Output: 8


'''
🧪 Task: Create a Class for Online Orders'''

'''
 Class: Order
✅ Requirements:
Instance Variables:

customer_name

items (a list)

total (initially 0)

Class Variable:

platform_name = "QuickBuy"

Instance Method:

add_item(item_name, price) → adds item to items list and updates total.

Class Method:

change_platform_name(new_name) → change the platform name for all orders.

Static Method:

calculate_gst(amount) → returns 18% of the given amount.

🔍 Sample Usage:
python
Copy
Edit
o1 = Order("Deepak")
o1.add_item("Mouse", 500)
o1.add_item("Keyboard", 1500)

gst = Order.calculate_gst(o1.total)
print("GST:", gst)

Order.change_platform_name("FastKart")
print("Platform:", Order.platform_name)
Try to:

Implement the class as per the requirements.

Test all three method types.

Once done, send your code here and I’ll review it before we move to the next topic: Encapsulation & Private Variables.

'''

class Order:

    platform_name = "QuickBuy"

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.total = 0

    def add_item(self, item_name, price):
        self.items.append(item_name)
        self.total += price

    @classmethod
    def change_platform_name(cls,new_name):
        cls.platform_name = new_name

    @staticmethod
    def calculate_gst(amount):
        return  .18*amount


print("\nExercise\n------------------------------")

o1 = Order("Deepak")
o1.add_item("Mouse", 500)
o1.add_item("Keyboard", 1500)

gst = Order.calculate_gst(o1.total)

print("Customer:", o1.customer_name)
print("Items:", o1.items)
print("Total:", o1.total)
print("GST:", gst)
print("Platform:", Order.platform_name)

# Changing platform name
Order.change_platform_name("FastKart")
print("New Platform:", Order.platform_name)



'''
Build a Student Grading System
📘 Class: Student
✅ 1. Instance Variables:
name

marks (list of numbers)

grade (default: None)

✅ 2. Class Variable:
school_name = "Bright Future School"

✅ 3. Instance Methods:
add_marks(m) → appends a mark to the marks list

calculate_average() → returns the average of the marks

assign_grade() → sets the grade based on average:

>90 → A

75–90 → B

50–75 → C

<50 → D

✅ 4. Class Method:
change_school(cls, name) → change the school for all students

✅ 5. Static Method:
is_valid_mark(mark) → returns True if mark is between 0 and 100, else False

🧪 Test the system:
Create 2 student objects.

Add some marks using add_marks().

Call assign_grade() for each.

Print:

Name

Average

Grade

School name

Also try giving an invalid mark and using is_valid_mark() to check it.

🔍 Output should look something like:
makefile
Copy
Edit
Name: Deepak
Average: 88.5
Grade: B
School: Bright Future School
Go ahead and code it when you're ready — then paste it here and
 I’ll review it carefully before we proceed to Encapsulation 
 & Private Variables.
'''

print("\nChallenge 2 \n-----------------------\n")


class Student:

    school_name = "Bright Future School"

    def __init__(self, name):
        self.name = name
        self.marks = []
        self.grade = None

    def add_mark(self,m):
        if self.is_valid_mark(m):
            self.marks.append(m)
        else:
            print(f"Invalid mark: {m}")
    
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
    
    def assign_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            self.grade = 'A'
        elif avg >= 75:
            self.grade = 'B'
        elif avg >= 50:
            self.grade = 'C'
        else:
            self.grade = 'D'


    @classmethod
    def change_school(cls, name):
        cls.school_name = name

    
    @staticmethod
    def is_valid_mark(mark):
        if mark>0 and mark<100:
            return True
        return False

    


s1 = Student("Deepak")
s1.add_mark(85)
s1.add_mark(90)
s1.add_mark(78)
s1.add_mark(-10)  # Invalid mark
s1.assign_grade()

print("Name:", s1.name)
print("Average:", s1.calculate_average())
print("Grade:", s1.grade)
print("School:", Student.school_name)

# Change school for all
Student.change_school("NextGen Academy")
print("Updated School:", Student.school_name)