'''
LCM
Difficulty: BasicAccuracy: 71.26%Submissions: 3K+Points: 1
Given two numbers a and b. The task is to find out their LCM.

Examples:

Input: a = 5, b = 10
Output: 10
Explanation: LCM of 5 and 10 is 10
Input: a = 14, b = 8
Output: 56
Explanation: LCM of 14 and 8 is 56
Constraints:
1  <=  a , b  <=  103'''

#User function Template for python3
a = int(input())
b = int(input())

# Your code here
lcm = max(a,b)

while True:
    if lcm%a ==0 and lcm%b ==0:
        break
    lcm+=1

print(lcm)


