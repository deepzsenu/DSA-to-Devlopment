'''
Print Square
Difficulty: BasicAccuracy: 52.18%Submissions: 4K+Points: 1
Given an integer n, write a program to print the square of size n using "*" character. 

Examples :

Input: n = 4
Output:
* * * *
*     *
*     *
* * * *
Explanation: It's a square! Each side contains n = 4 .
Input: n = 3
Output:
* * * 
*   *
* * *
Explanation: It's a square! Each side contains n = 3 .
Constraints:
1 ≤ n ≤ 10
'''

n = int(input())

for i in range(n):
    for j in range(n):
        if i== 0 or i == (n-1) or j ==0  or j == (n-1):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()