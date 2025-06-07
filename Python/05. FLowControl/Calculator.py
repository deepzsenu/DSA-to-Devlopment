'''
Calculator
Difficulty: EasyAccuracy: 63.9%Submissions: 6K+Points: 2
Given two numbers a and b. You need to perform basic mathematical operations on them. You will be provided an integer named as operator.

If the operator equals to 1 add a and b, then print the result.
If the operator equals to 2 subtract b from a, then print the result.
If the operator equals to 3 multiply a and b, then print the result.
If the operator equals to any other number, print "Invalid Input"(without quotes).
Note: Do not add a new line at the end.

Examples:

Input: a = 1, b = 2, operator = 3
Output: 2
Explanation: 1 * 2 = 2
Input: a = 2, b = 2, operator = 2
Output: 0
Explanation: 2 - 2 = 0
'''

class Solution:
    def calculate(self, a: int, b: int, operator: int) -> None:
        #code here
        
        if operator == 1:
            print(a+b, end = "")
            
        elif operator == 2 :
            print(a-b,end = "")
            
        elif operator == 3:
            print(a*b,end = "")
            
        else:
            print("Invalid Input",end = "")