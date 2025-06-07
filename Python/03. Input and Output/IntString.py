'''
Int Str
Difficulty: BasicAccuracy: 60.11%Submissions: 8K+Points: 1
Given three inputs that are stored in the variables a, b, and c. You need to print a 
a times and b b times  in a single line separated by c.

Examples:

Input: a = 6, b = 4, c = &
Output: 666666&4444
Explanation: 6 printed 6 times and 4 printed 4 times seperated by c = &
'''

#User function Template for python3
a = input()
b = input()
c = input()
# Write your code below that prints a a times and b b times, seperated by c

print(a*int(a),b*int(b), sep =c)