'''
Types of Arguments
Python supports various types of arguments that can be passed at the 
time of the function call. Let’s discuss each type in detail.

Default arguments
A default argument is a parameter that assumes a default value if a value 
is not provided in the function call for that argument. The following example illustrates
 Default arguments. 
'''

# Python program to demonstrate
# default arguments
def myFun(x, y=50):
	print("x: ", x)
	print("y: ", y)

# Driver code (We call myFun() with only
# argument)
myFun(10)