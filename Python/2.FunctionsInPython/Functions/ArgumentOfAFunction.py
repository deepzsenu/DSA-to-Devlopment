'''
Arguments of a Function
Arguments are the values passed inside the parenthesis of the function.
 A function can have any number of arguments separated by a comma.

Example: Python Function with arguments
In this example, we will create a simple function to check whether the number
 passed as an argument to the function is even or odd.
'''

# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")


# Driver code to call the function
evenOdd(2)
evenOdd(3)


