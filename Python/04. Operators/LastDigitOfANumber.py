'''
Last Digit of a number
Difficulty: BasicAccuracy: 49.19%Submissions: 12K+Points: 1
Given an integer n. Write a program to return the last digit of the number.

Examples:

Input: n = 10
Output: 0
Input: n = 9768
Output: 8
Constraints:

-109 ≤ n ≤ 109

'''
class Solution:
    def lastDigit(self, n: int) -> int:
        #Code here
        return abs(n)%10