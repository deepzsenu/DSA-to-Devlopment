'''
Rotate Array
Difficulty: MediumAccuracy: 37.06%Submissions: 514K+Points: 4Average Time: 20m
Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular.

Examples :

Input: arr[] = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]
Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.
Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]
Explanation: when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.
Input: arr[] = [7, 3, 9, 1], d = 9
Output: [3, 9, 1, 7]
Explanation: when we rotate 9 times, we'll get 3 9 1 7 as resultant array.
Constraints:
1 <= arr.size(), d <= 10^5
0 <= arr[i] <= 10^5

'''

#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        def reverse(start, end , arr):
            while (start < end):
                arr[start], arr[end] = arr[end], arr[start]
                start+=1
                end -=1
        start = 0 
        l = len(arr)
        d = d%l
        reverse(0,d-1,arr)
        reverse(d,l-1,arr)
        reverse(0,l-1, arr)
