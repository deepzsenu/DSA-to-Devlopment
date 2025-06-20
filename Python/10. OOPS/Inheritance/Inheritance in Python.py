'''
Inheritance in Python
🧠 What Is Inheritance?
Inheritance is the mechanism where one class (child/derived) inherits properties and methods from another class (parent/base).
This lets us reuse code, extend functionality, and model real-world relationships.

🔷 Why Use Inheritance?
- Avoids code duplication

- Follows DRY (Don’t Repeat Yourself) principle

- Enables extensibility of code

- Supports polymorphism (more on that later)
'''

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

obj = Child()
obj.greet()         # ✅ Inherited method
obj.greet_child()   # ✅ Child method


'''
👪 Types of Inheritance in Python
Type	              Example
Single	               One parent → one child
Multilevel	           Parent → Child → Grandchild
Multiple	           One child inherits from multiple parents
Hierarchical	       One parent → many children
Hybrid	               Mix of any of the above
'''



# Example – Single Inheritance:

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()   # from Animal
d.bark()    # from Dog



# Example – Multilevel Inheritance:

class A:
    def method_a(self): print("A")

class B(A):
    def method_b(self): print("B")

class C(B):
    def method_c(self): print("C")

obj = C()
obj.method_a()  # A → inherited


# 🔹 Example – Multiple Inheritance:

class Father:
    def skills(self):
        print("Math")

class Mother:
    def skills(self):
        print("Art")

class Child(Father, Mother):
    pass

c = Child()
c.skills()  # Output depends on method resolution order (MRO)

'''

 Method Resolution Order (MRO)
In multiple inheritance, Python looks for methods left to right:
'''
class A: pass
class B(A): pass
class C(B): pass
print(C.__mro__)  # Shows lookup path

'''

What is super() in Python?
super() is a built-in function used inside a child class to call methods of the parent class, especially within
 constructors (__init__) or overridden methods.

✅ Why use super()?
To reuse code from the parent class

To extend behavior instead of replacing it

Helps avoid redundancy and supports method resolution in multiple inheritance

🔧 Use Case 1: Calling Parent Constructor
'''
class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")

class Students(Person):
    def __init__(self, name, grade):
        super().__init__(name)  # calls Person.__init__
        self.grade = grade
        print("Student constructor called")

s = Students("Deepak", "A")
# 🧾 Output:

# Person constructor called  
# Student constructor called

# 🔧 Use Case 2: Extending a Method

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()  # calls Parent.show
        print("Child method")

c = Child()
c.show()
# 🧾 Output:

# Parent method  
# Child method

'''
🔁 How super() Helps in Multiple Inheritance
It respects MRO (Method Resolution Order), so when you have multiple parent classes, 
it ensures the correct sequence of method calls.
'''

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(B):
    def show(self):
        super().show()
        print("C")

c = C()
c.show()

# A  
# B  
# C
'''
This is because super() in C calls B.show(), which calls A.show() — clean and hierarchical.

🔒 Important Notes:
super() is typically used in overridden methods to call the base version.

It’s safest to use super() in modern Python (especially with multiple inheritance).

Avoid hardcoding the parent class name (like ParentClass.__init__(self, ...)) unless absolutely necessary.

✅ Summary
Feature	Benefit
super()	Calls methods from the parent class
Clean syntax	No need to hardcode parent class name
MRO-safe	Works well in multiple inheritance
Constructor chaining	Avoids duplicating init code
'''


'''
 Hierarchical Inheritance
In Hierarchical inheritance, multiple child classes inherit from a single parent class.

✅ Structure:

        Parent
       /   |   \
   Child1 Child2 Child3

🔧 Code Example:
'''

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

class Cow(Animal):
    def moo(self):
        print("Cow moos")

d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()

cw = Cow()
cw.eat()
cw.moo()
# 🧾 Output:

# Animal eats  
# Dog barks  
# Animal eats  
# Cat meows  
# Animal eats  
# Cow moos
'''
✅ All child classes reuse the eat() method from Animal, but have their own behaviors.

🧬 2. Hybrid Inheritance
Hybrid inheritance is a combination of two or more types of inheritance, often forming a complex hierarchy.

✅ Structure (Example: Multiple + Multilevel):

         A
        / \
       B   C
        \ /
         D
A: Base class

B and C inherit from A

D inherits from both B and C → Hybrid
'''

# 🔧 Code Example:

class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C(A):
    def show_c(self):
        print("Class C")

class D(B, C):  # Hybrid: D has multilevel + multiple
    def show_d(self):
        print("Class D")

d = D()
d.show_a()  # from A
d.show_b()  # from B
d.show_c()  # from C
d.show_d()  # from D
# 🧾 Output:

# Class A  
# Class B  
# Class C  
# Class D

'''
🔄 Method Resolution Order (MRO):
Check MRO using:
'''


print(D.__mro__)
'''
This shows how Python resolves which method to call if multiple parents have the same method name.

✅ Summary:
Inheritance Type	Description	Example Use Cases
Hierarchical	    One parent → many children	Common features reused
Hybrid	            Mix of any inheritance (multiple + multilevel, etc.)	Complex class structures

'''

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(B):
    pass

c = C()
c.show()



'''
Task: Student Performance System (Hybrid Inheritance)
🎯 You’ll build a system where:
One base class defines general Person info

Two child classes extend different roles (Student and Athlete)

One final class (ScholarAthlete) inherits from both

✅ Class Structure:
markdown
Copy
Edit
     Person
    /      \
Student   Athlete
    \      /
  ScholarAthlete
🛠️ Requirements:
class Person
Attributes: name, age

Method: show_person()

class Student(Person)
Attribute: marks

Method: show_student()

class Athlete(Person)
Attribute: sport

Method: show_athlete()

class ScholarAthlete(Student, Athlete)
Constructor: Initialize all attributes via super() and direct calls if needed

Method: show_all() → calls all three display methods

🔍 Sample Execution:

sa = ScholarAthlete("Deepak", 20, 88, "Football")
sa.show_all()
🔸 Expected Output:
makefile
Copy
Edit
Name: Deepak
Age: 20
Marks: 88
Sport: Football
'''
print("\n\n")

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, marks):
        Person.__init__(self, name, age)  # ❗️Use Person directly
        self.marks = marks

class Athlete(Person):
    def __init__(self, name, age, sports):
        Person.__init__(self, name, age)  # ❗️Use Person directly
        self.sports = sports

class ScholarAthlete(Student, Athlete):
    def __init__(self, name, age, marks, sports):
        Student.__init__(self, name, age, marks)
        Athlete.__init__(self, name, age, sports)

    def show_all(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Sports : {self.sports}")

# ✅ Run it
sa = ScholarAthlete("Deepak", 20, 88, "Football")
sa.show_all()

