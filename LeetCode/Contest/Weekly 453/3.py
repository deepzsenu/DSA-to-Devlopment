'''
Count Partitions With Max-Min Difference at Most K
Solved
Medium
premium lock icon
Companies
Hint
You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [9,4,1,3,7], k = 4

Output: 6

Explanation:

There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

[[9], [4], [1], [3], [7]]
[[9], [4], [1], [3, 7]]
[[9], [4], [1, 3], [7]]
[[9], [4, 1], [3], [7]]
[[9], [4, 1], [3, 7]]
[[9], [4, 1, 3], [7]]
Example 2:

Input: nums = [3,3,4], k = 0

Output: 2

Explanation:

There are 2 valid partitions that satisfy the given conditions:

[[3], [3], [4]]
[[3, 3], [4]]
 

Constraints:

2 <= nums.length <= 5 * 104
1 <= nums[i] <= 109
0 <= k <= 109
'''

from typing import List
from collections import deque

MOD = 10**9 + 7

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 1 way to partition empty prefix
        pre = [0] * (n + 1)
        pre[0] = 1
        
        doranisvek = []  # Store intermediate valid starting indices (optional debug)

        minDeque = deque()
        maxDeque = deque()

        left = 0
        for right in range(n):
            # Maintain min deque
            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()
            minDeque.append(right)

            # Maintain max deque
            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()
            maxDeque.append(right)

            # Move left pointer until valid window
            while nums[maxDeque[0]] - nums[minDeque[0]] > k:
                left += 1
                if minDeque[0] < left:
                    minDeque.popleft()
                if maxDeque[0] < left:
                    maxDeque.popleft()

            # Now [left..right] is valid window
            doranisvek.append(left)
            dp[right + 1] = (pre[right] - pre[left - 1] if left > 0 else pre[right]) % MOD
            pre[right + 1] = (pre[right] + dp[right + 1]) % MOD

        return dp[n]
