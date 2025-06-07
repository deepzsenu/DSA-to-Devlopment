'''
Docstring
The first string after the function is called the Document string or Docstring in short. 
This is used to describe the functionality of the function. The use of docstring in functions
 is optional but it is considered a good practice.

The below syntax can be used to print out the docstring of a function:

Syntax: print(function_name.__doc__)

Example: Adding Docstring to the function
'''

# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
	"""Function to check if the number is even or odd"""
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")

# Driver code to call the function
print(evenOdd.__doc__)

