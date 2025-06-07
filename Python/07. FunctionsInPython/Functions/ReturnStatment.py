'''
The return statement
The function return statement is used to exit from a function and go back to the function caller and return the specified value or data item to the caller.

Syntax: return [expression_list]
The return statement can consist of a variable, an expression, or a constant which is returned to the end of the function execution. If none of the above is present with the return statement a None object is returned.

Example: Python Function Return Statement
'''

def square_value(num):
	"""This function returns the square value of the entered number"""
	return num**2

print(square_value(2))
print(square_value(-4))

