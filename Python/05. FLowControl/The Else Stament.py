'''
The Else Statement
Difficulty: BasicAccuracy: 72.95%Submissions: 6K+Points: 1
Given an integer a, you have to use the if statement to print "Big" (without quotes) if the given number is greater than 100, and use the else statement to print "Number" (without quotes) when the number is smaller than or equal to 100.

Note: After printing the output, you should move the cursor to the new line.

Examples:

Input: a = 10
Output: Number
Explanation: 10 is smaller than 100, so our else statement works and we print Number.
Input: a = 101
Output: Big
Explanation: 101 is greater than 100, so our if statement works and we print Big.'''
#User function Template for python3
n = int(input())
if n <= 100:
    print("Number")
else:
    print("Big")