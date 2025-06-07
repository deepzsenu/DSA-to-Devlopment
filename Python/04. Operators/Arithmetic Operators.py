'''


Arithmetic Operators
Difficulty: BasicAccuracy: 64.71%Submissions: 9K+Points: 1
You are given two integer variables x and y. You need to perform the following operations:

p = x + y : Addition
q = x - y : Subtraction
r = x * y :Multiplication
s = x / y : Division
t = x % y : Modulo
Examples:

Input: x = 1, y = 2
Output: 3 -1 2 0 1 
Explanation: The given operations are performed.
Input: x = 3, y = 4 
Output: 7 -1 12 0 3 
Explanation: The given operations are performed

'''

#User function Template for python3
x=int(input())
y=int(input())

########### Write your code below ###############
# Perform addition x+y below
p = x+y
# Perform subtraction x-y below
q = x-y
# Perform multiplication x*y below
r =  x*y
# Perform integer divison x//y below
s = x//y
# Perform modulo operation x%y below
t = x%y
########### Write your code above ###############

#The below code prints the output. Don't change it!
print(p, q, r, s, t)