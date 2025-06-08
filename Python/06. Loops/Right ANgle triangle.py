'''
Right Angle Triangle
Difficulty: BasicAccuracy: 68.08%Submissions: 2K+Points: 1
Given an integer n. Write a program to print the Right angle triangle wall. The length of perpendicular and base is n.  Use single loop and string multiplication.

Note: Print exactly single " " after "*". Print a new line after printing the triangle.

Examples:

Input: n = 4
Output:
* 
* * 
* * * 
* * * * 
Explanation: Length of perpendicular and base of triangle is 4 .
Input: n = 3
Output:
* 
* * 
* * * 
Explanation: Length of perpendicular and base of triangle is 3 .
Constraints:
1 ≤ s ≤ 10'''
#User function Template for python3
n = int(input())

# Your code here

for i in range(1,n+1):
    print(i*"* ")
