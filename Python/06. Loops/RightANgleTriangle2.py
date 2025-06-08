'''
Right Angle Triangle 2
Difficulty: EasyAccuracy: 52.76%Submissions: 4K+Points: 2
Given an integer n. Write a program to print the Right angle triangle. The length of the perpendicular and base is n.  

Examples :

Input: n = 9
Output:
*
* *
*   *
*     *
*       *
*         *
*           *
*             *
* * * * * * * * * 
Explanation: Length of perpendicular and base of triangle is 9.
Input: n = 4
Output:
*
* *
*   *
* * * *
Explanation: Length of perpendicular and base of triangle is 4.
Constraints:
1 ≤ n ≤ 12


'''

class Solution:
    def printPattern(self, n):
        #Code here

        for i in range(n):
            for j in range(n):
                if j == 0  or i == j or i == n-1:
                    print("*", end = " ")
                elif j<i:
                    print(" ", end = " ")
            print()