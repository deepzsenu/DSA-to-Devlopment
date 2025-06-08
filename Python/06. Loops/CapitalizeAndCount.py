'''
Capitalize and Count
Difficulty: EasyAccuracy: 79.4%Submissions: 1K+Points: 2
Given a string s of single space-separated words. Capitalize the first letter of all words and count the number of the words in the string. Print the line and the number in separate lines with new line character at the end.

Examples:

Input: s = "welcome to the world of geeks"
Output: 
Welcome To The World Of Geeks
6
Input: s = "are you enjoying programming"
Output:
Are You Enjoying Programming
4
'''

#User function Template for python3
s = input()
count = 1
# Your code here
if s == "":
    print(0)
else:
    cap = ' '.join(word.capitalize() for word in s.split())
    count = len(s.split())
    print(cap)

    print(count)
