'''
Anonymous functions: 
In Python, an anonymous function means that a function is without a name. 
As we already know the def keyword is used to define the normal functions and the 
lambda keyword is used to create anonymous functions. Please see this for details.
'''

# Python code to illustrate the cube of a number
# using lambda function


def cube(x):
    return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))