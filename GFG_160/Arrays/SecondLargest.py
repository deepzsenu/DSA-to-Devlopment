'''
Second Largest
Difficulty: EasyAccuracy: 26.72%Submissions: 1.2MPoints: 2Average Time: 15m
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.
Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
'''

def getSecondLargest(arr):
    largest = float("-inf")
    secLargest = float("-inf")

    for i in range(len(arr)):
        if arr[i] > largest:
            secLargest= largest
            largest = arr[i]
        elif arr[i]<largest and arr[i] > secLargest:
            secLargest = arr[i]
    return secLargest

arr = [4,5,2,1,5,5,6,77,73,2,32,2,3,43,43,342,2323,23,3,444,5]

print(getSecondLargest(arr))
