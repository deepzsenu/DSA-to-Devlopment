'''
For Loop - 2
Difficulty: BasicAccuracy: 69.31%Submissions: 4K+Points: 1
You are given a string s, you need to print its characters at even indices (index starts at 0).

Examples:

Input: s = "Geeks"
Output: Ges
Explanation: The even indices characters are printed.
Input: s = "DoctorPhenomenal"
Output: DcoPeoea
Explanation: The even indices characters are printed.
'''

class Solution:
    def print_even_indices(self, s: str):
        #code here

        for i in range(len(s)):
            if i%2 == 0:
                print(s[i], end ="")
