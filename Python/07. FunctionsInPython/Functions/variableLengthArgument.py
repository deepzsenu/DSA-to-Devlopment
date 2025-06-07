'''
Variable-length arguments
In Python, we can pass a variable number of arguments to a function using special symbols. 
There are two special symbols:

1. *args (Non-Keyword Arguments)
2. **kwargs (Keyword Arguments)

Example 1: Variable length non-keywords argument
'''
# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
	for arg in argv:
		print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

'''Example 2: Variable length keyword arguments'''
# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))

# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

# More examples to demonstrate better

def userProfile(**kwargs):
    print("User Profile:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

userProfile(name="Deepak", age=25, city="Delhi", profession="Engineer")

'''2. Mixing *args and **kwargs:'''
def showData(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

showData(1, 2, 3, name="John", city="Mumbai")

'''3. Using **kwargs to pass settings to a function:'''
def displaySettings(**settings):
    for setting, value in settings.items():
        print(f"{setting} is set to {value}")

displaySettings(volume="High", brightness="80%", wifi="On")


'''4. Function forwarding using **kwargs:'''
def greet(**kwargs):
    print("Hello", kwargs.get("name", "Guest"))

def startApp():
    greet(name="Alice")

startApp()

'''5. Passing a dictionary using **:'''
def employeeInfo(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

data = {'name': 'Ravi', 'id': 102, 'role': 'Manager'}
employeeInfo(**data)
