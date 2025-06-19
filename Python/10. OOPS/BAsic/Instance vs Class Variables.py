"""
Instance Variables — Your Personal Backpack 🎒
🔍 Definition:
Instance variables are unique to each object of a class.
They are declared using self., usually in the __init__() method.

"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Deepak", 90)
s2 = Student("Aman", 75)

# print(s1.name, s1.marks)  # Deepak 90
# print(s2.name, s2.marks)  # Aman 75


#  Internally:
# s1 has its own name and marks

# s2 has separate name and marks

# Changing s1.marks won’t affect s2.marks.


'''
Class Variables — Shared Whiteboard 📋
🔍 Definition:
Class variables are shared across all objects of the class.
They are defined directly inside the class, outside any method.

'''

class Student:
    school_name = "ABC Public School"  # Class variable

    def __init__(self, name):
        self.name = name

s1 = Student("Deepak")
s2 = Student("Aman")

# print(s1.school_name)  # ABC Public School
# print(s2.school_name)  # ABC Public School


# Both s1 and s2 refer to the same school_name.

# Changing it at the class level changes it for all objects.

# Bonus: How to View Them Clearly?

# print(s1.__dict__)  # shows only instance variables
# print('\n')
# print(Student.__dict__)  # shows class attributes (including methods)


'''
Practice Task: Create a Class for Library Books
📚 Requirements:
Create a class called Book.

Add a class variable called library_name with the value "Central Library".

In the constructor (__init__), take title, author, and pages as instance variables.

Create a method display_info() that prints:

Book title

Author name

Number of pages

Library name (from class variable)

📌 Example Output:
python
Copy
Edit
b1 = Book("1984", "George Orwell", 328)
b2 = Book("Python Basics", "John Doe", 200)

b1.display_info()

# Output:
# Title: 1984
# Author: George Orwell
# Pages: 328
# Library: Central Library
Also try changing Book.library_name = "City Library" and call display_info() again to
 see the change across all objects.


'''

class  Book:
    library_name = "Central Library"

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Library: {self.library_name}")


b1 = Book("1984", "George Orwell", 328)
b2 = Book("Python Basics", "John Doe", 200)

b1.display_info()

print("\nChanging library name...\n")
Book.library_name = "City Library"
b2.display_info()