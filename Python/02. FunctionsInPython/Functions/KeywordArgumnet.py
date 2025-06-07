'''
Keyword arguments
The idea is to allow the caller to specify the argument name with values so that 
caller does not need to remember the order of parameters.
'''
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
	print(firstname, lastname)

# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')