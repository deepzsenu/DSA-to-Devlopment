'''
You are given two variables, a and b. Your task is to print these variables in the following formats:

With space: Print a and b in a single line, separated by a space, followed by a newline.
Without newline: Print a and b separated by a space, but do not end the output with a newline.
With separator: Print a and b separated by a specified separator, followed by a newline.
Without space: Print a and b in a single line, with no spaces between them, followed by a newline.
Examples:

Input: a = "Hello", b = "World", separator = '&'
Output: 
Hello World
Hello WorldHello&World
HelloWorld
Explanation: 
With space: a and b are printed in a single line with a space separating them. (Hello World)
Without newline: a and b are printed in a single line with a space separating them, but no newline is added after. (Hello World with no newline).
With separator: a and b are printed in a single line, separated by the given separator character. (Hello&World)
Without space: a and b are printed directly next to each other with no space between them. (HelloWorld)
'''
#User function Template for python3
a = input()
b = input()
separator = input()[0]

########### Write your code below ###############

# Print with space
print(a,b,sep=" ")

# Print without newline at the end
print(a,b,end="")

# Print with separator
print(a,b, sep=separator)


# Print without space
print(a,b,sep = "")

########### Write your code above ###############

