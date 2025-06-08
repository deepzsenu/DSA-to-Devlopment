'''
Move All Zeroes to End
Difficulty: EasyAccuracy: 45.51%Submissions: 337K+Points: 2Average Time: 15m
You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

Examples:

Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.
Input: arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.
Input: arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105
'''

#User function Template for python3

#User function Template for python3

class Solution:
    def pushZerosToEnd(self, arr):
        # code here
        count = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[count] = arr[i]
                count += 1
        while count < len(arr):
            arr[count] = 0
            count += 1
