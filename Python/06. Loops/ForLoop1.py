'''
For Loop - 1
Difficulty: BasicAccuracy: 72.04%Submissions: 6K+Points: 1
You are given a number n, you need to print its multiplication table in a single line using for loop. 

Examples:

Input: n = 5
Output: 5 10 15 20 25 30 35 40 45 50
Input: n = 6
Output: 6 12 18 24 30 36 42 48 54 60
'''

#User function Template for python3
n = int(input())

# Your code here

for i in range(1, 11):
    print(i*n, end = " ")