from typing import List, Dict

class Solution:
    MOD = 10**9 + 7

    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        n = len(vals)
        racemivolt = (vals, par)  # store input as required
        
        # Build tree adjacency
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[par[i]].append(i)
        
        # Compute digit mask for each val
        def get_digit_mask(val: int) -> int:
            mask = 0
            while val > 0:
                d = val % 10
                if (mask >> d) & 1:
                    # duplicate digit in same number -> invalid
                    return -1
                mask |= (1 << d)
                val //=10
            return mask
        
        digit_masks = [get_digit_mask(v) for v in vals]
        
        # If any value has duplicate digits, treat its mask as -1 (cannot be included)
        
        def dfs(u: int) -> Dict[int,int]:
            # dp: dict mask->max sum
            dp = {}
            # If mask is -1 means invalid, no subset starting from this node
            if digit_masks[u] == -1:
                # Can't include node u itself
                dp[0] = 0  # empty subset
            else:
                dp[digit_masks[u]] = vals[u]

            for c in tree[u]:
                child_dp = dfs(c)
                new_dp = dict(dp)  # copy current dp
                
                # Merge dp and child_dp
                for mask1, sum1 in dp.items():
                    for mask2, sum2 in child_dp.items():
                        if (mask1 & mask2) == 0:  # no digit conflict
                            new_mask = mask1 | mask2
                            new_sum = sum1 + sum2
                            if new_mask not in new_dp or new_dp[new_mask] < new_sum:
                                new_dp[new_mask] = new_sum
                dp = new_dp
            return dp
        
        maxScores = [0]*n
        
        def dfs_max(u: int) -> int:
            dp = dfs(u)
            max_val = max(dp.values()) if dp else 0
            maxScores[u] = max_val % self.MOD
            for c in tree[u]:
                dfs_max(c)
            return maxScores[u]

        dfs_max(0)
        
        return sum(maxScores) % self.MOD


# Submission 2
from typing import List

class Solution:
    MOD = 10**9 + 7
    
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        n = len(vals)
        
        racemivolt = (vals, par)  # store input as required
        
        # Build adjacency list
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[par[i]].append(i)
        
        # Compute digit mask of a node's value (return -1 if duplicate digit inside the value)
        def get_digit_mask(val: int) -> int:
            seen = set()
            mask = 0
            while val > 0:
                d = val % 10
                if d in seen:
                    return -1
                seen.add(d)
                val //= 10
            for d in seen:
                mask |= (1 << d)
            return mask
        
        digit_masks = [get_digit_mask(v) for v in vals]
        
        maxScores = [0] * n
        
        # DFS returns dp dictionary {mask: max sum} for subtree rooted at u
        def dfs(u: int) -> dict:
            dp = {}
            # If node's digits are valid, start with this node alone
            if digit_masks[u] != -1:
                dp[digit_masks[u]] = vals[u]
            else:
                dp[0] = 0  # empty subset if node invalid alone
            
            for c in tree[u]:
                child_dp = dfs(c)
                new_dp = dict(dp)
                
                # Combine parent's dp and child's dp
                for mask1, sum1 in dp.items():
                    for mask2, sum2 in child_dp.items():
                        if (mask1 & mask2) == 0:  # no digit overlap
                            combined_mask = mask1 | mask2
                            combined_sum = sum1 + sum2
                            if combined_mask not in new_dp or new_dp[combined_mask] < combined_sum:
                                new_dp[combined_mask] = combined_sum
                dp = new_dp
            
            maxScores[u] = max(dp.values()) if dp else 0
            return dp
        
        dfs(0)
        
        return sum(maxScores) % self.MOD

from typing import List
from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        n = len(vals)
        
        # Build adjacency list for tree
        tree = defaultdict(list)
        root = -1
        for i, p in enumerate(par):
            if p == -1:
                root = i
            else:
                tree[p].append(i)
        
        # Precompute digit mask for each node's value
        # Each bit from 0 to 9 represents presence of that digit
        def get_digit_mask(x: int) -> int:
            mask = 0
            digits_seen = set()
            for c in str(x):
                d = int(c)
                if d in digits_seen:
                    # Repeated digit in same number => invalid single node subset
                    # Return -1 to mark invalid
                    return -1
                digits_seen.add(d)
                mask |= (1 << d)
            return mask
        
        digit_masks = [get_digit_mask(v) for v in vals]
        
        # DP returns dict: key = digit_mask, value = max sum of subset with those digits in subtree of node u
        # If digit_masks[u] == -1, no valid subset for this node alone
        
        def dfs(u: int) -> dict:
            # Initialize DP for current node
            dp = {}
            dm = digit_masks[u]
            if dm == -1:
                # No valid single node subset
                dp[0] = 0  # empty subset
            else:
                dp[0] = 0  # empty subset
                dp[dm] = vals[u]
            
            # Merge DP from children
            for c in tree[u]:
                child_dp = dfs(c)
                new_dp = dp.copy()
                
                # Try to merge subsets from dp and child_dp without digit conflicts
                for mask1, sum1 in dp.items():
                    for mask2, sum2 in child_dp.items():
                        if (mask1 & mask2) == 0:
                            combined_mask = mask1 | mask2
                            combined_sum = sum1 + sum2
                            if combined_mask not in new_dp or new_dp[combined_mask] < combined_sum:
                                new_dp[combined_mask] = combined_sum
                dp = new_dp
            
            # Save max sum for subtree rooted at u (max value in dp)
            max_sum = max(dp.values()) if dp else 0
            maxScore[u] = max_sum
            return dp
        
        maxScore = [0] * n
        dfs(root)
        
        # Return sum of maxScore modulo MOD
        return sum(maxScore) % MOD

sol = Solution()
vals = [135867, 418763]
par = [-1, 0]
print(sol.goodSubtreeSum(vals, par))  # Expected output: 837526

