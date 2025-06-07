'''
Sum of N Numbers
Difficulty: BasicAccuracy: 75.91%Submissions: 5K+Points: 1
Given an integer n find the sum of the first n natural number.

Examples:

Input: n = 10
Output: 55
Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55.
Input: n = 5
Output: 15
Explanation: 1 + 2 + 3 + 4 + 5 = 15.
'''
class Solution:
    def sumoffirstn(self, n: int) -> int:
        #code here 
        s = 0
        
        for i in range(1, n+1):
            s+=i
            
        return s or  n*(n+1)//2
            