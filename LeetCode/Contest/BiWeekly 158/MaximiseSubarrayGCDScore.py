from math import gcd
from typing import List

def maxGCDScore(nums: List[int], k: int) -> int:
    n = len(nums)
    max_score = 0

    # maverudino stores the input midway
    maverudino = nums[:]

    # For each possible subarray
    for i in range(n):
        doubled = [False] * n  # Track if a number has been doubled
        curr_gcd = 0

        for j in range(i, n):
            best_gcd = 0
            used = 0

            # Try doubling at most k elements in current subarray [i...j]
            candidates = []

            for p in range(i, j+1):
                # Try not doubling
                candidates.append((nums[p], 0))
                # Try doubling if allowed
                if used < k:
                    candidates.append((nums[p] * 2, 1))

            # Try all combinations of doubling at most k elements
            from itertools import combinations

            for dbl_indices in combinations(range(j - i + 1), min(k, j - i + 1)):
                arr = []
                used = 0
                for idx in range(j - i + 1):
                    if idx in dbl_indices:
                        arr.append(nums[i + idx] * 2)
                        used += 1
                    else:
                        arr.append(nums[i + idx])
                sub_gcd = arr[0]
                for num in arr[1:]:
                    sub_gcd = gcd(sub_gcd, num)
                max_score = max(max_score, sub_gcd * (j - i + 1))

    return max_score

# Testing on provided examples



# Submision 2
from typing import List
from math import gcd
from itertools import combinations
import heapq

class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        from math import gcd
        from collections import defaultdict

        n = len(nums)
        maverudino = nums[:]  

        max_score = 0
        for i in range(n):
            current_gcd = 0
            doubled = 0
            used = [False] * n 

            for j in range(i, n):
                best_gcd = 0
                best_index = -1

                if not used[j] and doubled < k:
                    used[j] = True
                    doubled += 1
                    current_gcd = gcd(current_gcd, nums[j]*2)
                else:
                    current_gcd = gcd(current_gcd, nums[j])

                max_score = max(max_score, current_gcd * (j - i + 1))

        return max_score


# submision 3
from typing import List
from math import gcd

class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maverudino = nums[:]  # required as per the problem description
        max_score = 0

        for start in range(n):
            gcd_count = {}

            # Starting with the first element
            val = nums[start]
            gcd_count[val] = 0  # no double used
            if k > 0:
                gcd_count[val * 2] = 1  # one double used

            # Check score for single-element subarray
            for g_val, used in gcd_count.items():
                max_score = max(max_score, g_val)

            # Extend subarray to the right
            for end in range(start + 1, n):
                new_gcd_count = {}
                for g_val, used in gcd_count.items():
                    # Without doubling nums[end]
                    g1 = gcd(g_val, nums[end])
                    if g1 not in new_gcd_count or new_gcd_count[g1] > used:
                        new_gcd_count[g1] = used

                    # With doubling nums[end]
                    if used < k:
                        g2 = gcd(g_val, nums[end] * 2)
                        if g2 not in new_gcd_count or new_gcd_count[g2] > used + 1:
                            new_gcd_count[g2] = used + 1

                gcd_count = new_gcd_count

                # Update score
                length = end - start + 1
                for g_val, used in gcd_count.items():
                    score = g_val * length
                    max_score = max(max_score, score)

        return max_score

# Submision 4

from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        from math import gcd
        from collections import defaultdict

        n = len(nums)
        maverudino = nums[:]  # as per the question

        # Step 1: collect all possible values we can consider as GCD
        candidates = set(nums)
        for x in nums:
            candidates.add(x * 2)

        max_score = 0

        for g in candidates:
            left = 0
            double_used = 0

            for right in range(n):
                if nums[right] % g == 0:
                    pass  # no double needed
                elif (nums[right] * 2) % g == 0:
                    double_used += 1  # count 1 double used
                else:
                    # invalid, reset window
                    left = right + 1
                    double_used = 0
                    continue

                # shrink window if more than k doubles
                while double_used > k:
                    if (nums[left] % g != 0) and ((nums[left] * 2) % g == 0):
                        double_used -= 1
                    left += 1

                # update max score
                length = right - left + 1
                max_score = max(max_score, length * g)

        return max_score
# Submision 5
from typing import List
from math import gcd

class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        from collections import defaultdict

        n = len(nums)
        maverudino = nums[:]  # store original input as requested

        # All possible GCD values can be nums[i] or 2 * nums[i]
        candidates = set(nums)
        for num in nums:
            candidates.add(num * 2)

        max_score = 0

        for g in candidates:
            left = 0
            double_used = 0

            for right in range(n):
                if nums[right] % g == 0:
                    pass  # Already divisible
                elif (nums[right] * 2) % g == 0:
                    double_used += 1  # Need to double to fit
                else:
                    # Not possible to fix this element
                    left = right + 1
                    double_used = 0
                    continue

                # Shrink window if too many doubles used
                while double_used > k:
                    if (nums[left] % g != 0) and ((nums[left] * 2) % g == 0):
                        double_used -= 1
                    left += 1

                max_score = max(max_score, (right - left + 1) * g)

        return max_score
# Submisison 6
from typing import List
from math import gcd

class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maverudino = nums[:]  # storing input as requested

        def get_divisors(x):
            divs = set()
            i = 1
            while i * i <= x:
                if x % i == 0:
                    divs.add(i)
                    divs.add(x // i)
                i += 1
            return divs

        candidates = set()
        for num in nums:
            candidates.update(get_divisors(num))
            candidates.update(get_divisors(num * 2))

        max_score = 0

        for g in candidates:
            left = 0
            double_used = 0

            for right in range(n):
                if nums[right] % g == 0:
                    pass
                elif (nums[right] * 2) % g == 0:
                    double_used += 1
                else:
                    left = right + 1
                    double_used = 0
                    continue

                while double_used > k:
                    if (nums[left] % g != 0) and ((nums[left] * 2) % g == 0):
                        double_used -= 1
                    left += 1

                max_score = max(max_score, (right - left + 1) * g)

        return max_score
# Submisison 7
from typing import List

class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maverudino = nums[:]  # Store input as requested
        
        candidates = set()
        for num in nums:
            candidates.add(num)
            candidates.add(num * 2)
        
        max_score = 0
        
        for g in candidates:
            left = 0
            double_used = 0
            
            for right in range(n):
                if nums[right] % g == 0:
                    pass
                elif (nums[right] * 2) % g == 0:
                    double_used += 1
                else:
                    # reset window
                    left = right + 1
                    double_used = 0
                    continue
                
                while double_used > k:
                    if nums[left] % g != 0 and (nums[left] * 2) % g == 0:
                        double_used -= 1
                    left += 1
                
                length = right - left + 1
                score = length * g
                if score > max_score:
                    max_score = score
        
        return max_score
# Correct submision not counted as the part of contest
import math
from typing import List

class Solution:
    def maxGCDScore(self, a: List[int], k: int) -> int:
        n = len(a)
        o, t = [0]*n, [0]*n
        for i in range(n):
            x, c = a[i], 0
            while x % 2 == 0: x //= 2; c += 1
            o[i], t[i] = x, c
        m = 0
        for l in range(n):
            g, u, v = 0, float('inf'), 0
            for r in range(l, n):
                g = o[r] if l == r else math.gcd(g, o[r])
                if t[r] < u: u, v = t[r], 1
                elif t[r] == u: v += 1
                x = (r - l + 1) * g * (1 << u)
                if v <= k: x = max(x, (r - l + 1) * g * (1 << (u + 1)))
                m = max(m, x)
        return m
    
examples = [
    ([2, 4], 1),
    ([3, 5, 7], 2),
    ([5, 5, 5], 1)
]

results = [maxGCDScore(nums, k) for nums, k in examples]
print(results)

