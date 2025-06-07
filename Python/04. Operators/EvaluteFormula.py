'''
Evaluate Formulae
Difficulty: BasicAccuracy: 73.52%Submissions: 5K+Points: 1
Given four inputs that are stored in variables a, b, c, and d. You need to write an expression to evaluate the following formula. Use integer division. The expression should be a single statement.



Examples:

Input: a = 10, b = 4, c = 7, d = 9
Output: 11
Explanation: 10 + 4 = 14, 14 // 7 = 2(Python) or 14 / 7 = 2(Java or CPP or C), 2 + 9 = 11.
'''

class Solution:
    def calculate(self, a: int, b: int, c: int, d: int) -> int:
        #Code here
        return ((a+b)//c)+d