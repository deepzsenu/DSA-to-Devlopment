'''
Swap The Numbers
Difficulty: SchoolAccuracy: 50.41%Submissions: 23K+Points: 0
Given two numbers a and b, you need to swap their values so a holds the value of
 b and b holds the value of a. Just write the code to swap values of a and b at the 
 specified place.

Examples

Input: a = 1, b = 2
Output: 2 1
Explanation: Initially a = 1 and b = 2, now a = 2 and b = 1.
Input: a = 6, b = 7  
Output: 7 6 
Explanation: Initially a = 6 and b = 7, now a = 7 and b = 6.

'''

# Method1
a = 2
b = 3

########### Write your code below ###############

# Write Code to Swap
a,b = b,a

########### Write your code above ###############

print(a, b)


#Method 2
temp = b
b = a
a = temp
print (a, b)

