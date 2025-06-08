'''
Table Difference
Difficulty: BasicAccuracy: 83.51%Submissions: 3K+Points: 1
Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2 and print in a single line.
Note: Don't add a new line in the end.

Example :

Input: n1 = 9, n2 = 4
Output: 5 10 15 20 25 30 35 40 45 50 
Explanation:
  9 18 27 36 45 54 63 72 81 90
- 4  8 12 16 20 24 28 32 36 40
-----------------------------------------
= 5 10 15 20 25 30 35 40 45 50
Input: n1 = 6, n2 = 2
Output: 5 10 15 20 25 30 35 40 45 50 
Explanation:
  6 12 18 24 30 36 42 48 54 60
- 2  4  6  8 10 12 14 16 18 20
-----------------------------------------
= 4  8 12 16 20 24 28 32 36 40
Constraints:
1  ≤  n1 , n2  ≤  106
'''

#User function Template for python3
n1 = int(input())
n2 = int(input())

# Your code here

for i in range(1,10+1):
    print((n1-n2)*i, end = " ")


