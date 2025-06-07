from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2:
            return 0

        # dp[day][transactions][state]
        # state: 0 = nothing held, 1 = normal buy held, 2 = short sell held
        dp = [[[float('-inf')] * 3 for _ in range(k + 1)] for _ in range(n)]
        
        # Base case: Day 0, 0 transactions, nothing held
        for t in range(k + 1):
            dp[0][t][0] = 0  # No action

        if k > 0:
            dp[0][1][1] = -prices[0]  # Buy
            dp[0][1][2] = prices[0]   # Short sell

        for day in range(1, n):
            for t in range(k + 1):
                # Case 0: not holding anything today
                dp[day][t][0] = dp[day - 1][t][0]  # do nothing
                if t > 0:
                    # sell if we had bought earlier
                    dp[day][t][0] = max(dp[day][t][0], dp[day - 1][t][1] + prices[day])
                    # buy back if we had short sold earlier
                    dp[day][t][0] = max(dp[day][t][0], dp[day - 1][t][2] - prices[day])

                # Case 1: holding a normal bought stock
                if t > 0:
                    dp[day][t][1] = max(dp[day - 1][t][1], dp[day - 1][t - 1][0] - prices[day])

                # Case 2: holding a short sell position
                if t > 0:
                    dp[day][t][2] = max(dp[day - 1][t][2], dp[day - 1][t - 1][0] + prices[day])

        # Get max profit on last day, not holding anything
        return max(dp[n - 1][t][0] for t in range(k + 1))

# Example 1
prices1 = [1, 7, 9, 8, 2]
k1 = 2
print(Solution().maximumProfit(prices1, k1))  # Output: 14

# Example 2
prices2 = [12, 16, 19, 19, 8, 1, 19, 13, 9]
k2 = 3
print(Solution().maximumProfit(prices2, k2))  # Output: 36
