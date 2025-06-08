'''
Minimum Steps to Convert String with Operations
Solved
Hard
premium lock icon
Companies
Hint
You are given two strings, word1 and word2, of equal length. You need to transform word1 into word2.

For this, divide word1 into one or more contiguous substrings. For each substring substr you can perform the following operations:

Replace: Replace the character at any one index of substr with another lowercase English letter.

Swap: Swap any two characters in substr.

Reverse Substring: Reverse substr.

Each of these counts as one operation and each character of each substring can be used in each type of operation at most once (i.e. no single index may be involved in more than one replace, one swap, or one reverse).

Return the minimum number of operations required to transform word1 into word2.

 

Example 1:

Input: word1 = "abcdf", word2 = "dacbe"

Output: 4

Explanation:

Divide word1 into "ab", "c", and "df". The operations are:

For the substring "ab",
Perform operation of type 3 on "ab" -> "ba".
Perform operation of type 1 on "ba" -> "da".
For the substring "c" do no operations.
For the substring "df",
Perform operation of type 1 on "df" -> "bf".
Perform operation of type 1 on "bf" -> "be".
Example 2:

Input: word1 = "abceded", word2 = "baecfef"

Output: 4

Explanation:

Divide word1 into "ab", "ce", and "ded". The operations are:

For the substring "ab",
Perform operation of type 2 on "ab" -> "ba".
For the substring "ce",
Perform operation of type 2 on "ce" -> "ec".
For the substring "ded",
Perform operation of type 1 on "ded" -> "fed".
Perform operation of type 1 on "fed" -> "fef".
Example 3:

Input: word1 = "abcdef", word2 = "fedabc"

Output: 2

Explanation:

Divide word1 into "abcdef". The operations are:

For the substring "abcdef",
Perform operation of type 3 on "abcdef" -> "fedcba".
Perform operation of type 2 on "fedcba" -> "fedabc".


Constraints:

1 <= word1.length == word2.length <= 100
word1 and word2 consist only of lowercase English letters.
'''

from functools import cache
from collections import Counter

class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        tronavilex = (word1, word2)

        @cache
        def dp(i):
            if i == n:
                return 0
            res = float('inf')
            for j in range(i + 1, n + 1):
                cost = self.segment_cost(word1[i:j], word2[i:j])
                res = min(res, cost + dp(j))
            return res

        return dp(0)

    def segment_cost(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        return min(
            self._segment_cost_core(s1, s2),
            1 + self._segment_cost_core(s1[::-1], s2)
        )

    def _segment_cost_core(self, s1: str, s2: str) -> int:

        mismatch = [(a, b) for a, b in zip(s1, s2) if a != b]
        count = Counter(mismatch)
        swaps = 0
        replaces = 0

        for (a, b) in list(count.keys()):
            if (b, a) in count:
                pair_count = min(count[(a, b)], count[(b, a)])
                swaps += pair_count
                count[(a, b)] -= pair_count
                count[(b, a)] -= pair_count

        replaces = sum(count.values())

        return swaps + replaces
