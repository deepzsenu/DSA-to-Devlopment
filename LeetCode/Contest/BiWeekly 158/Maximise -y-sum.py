from typing import List

class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        x_to_max_y = {}

        # Step 1: Map each x to its maximum y
        for xi, yi in zip(x, y):
            if xi not in x_to_max_y:
                x_to_max_y[xi] = yi
            else:
                x_to_max_y[xi] = max(x_to_max_y[xi], yi)

        # Step 2: Check if we have at least 3 distinct x values
        if len(x_to_max_y) < 3:
            return -1

        # Step 3: Get top 3 max y values
        top_y_values = sorted(x_to_max_y.values(), reverse=True)[:3]

        return sum(top_y_values)

# Create test inputs
test_cases = [
    {
        "x": [1, 2, 1, 3, 2],
        "y": [5, 3, 4, 6, 2],
        "expected": 14
    },
    {
        "x": [1, 2, 1, 2],
        "y": [4, 5, 6, 7],
        "expected": -1
    }
]

# Run test cases
solution = Solution()
for i, test in enumerate(test_cases, 1):
    result = solution.maxSumDistinctTriplet(test["x"], test["y"])
    print(f"Test Case {i}: Expected = {test['expected']}, Got = {result}, {'PASS' if result == test['expected'] else 'FAIL'}")
