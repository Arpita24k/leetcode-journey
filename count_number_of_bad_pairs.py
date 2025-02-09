from collections import defaultdict

class Solution:
    def countBadPairs(self, nums):
        """
        Returns the total number of bad pairs in nums.

        Args:
        nums (List[int]): List of integers.

        Returns:
        int: Count of bad pairs.
        """
        total_pairs = len(nums) * (len(nums) - 1) // 2  # Total possible pairs
        count_map = defaultdict(int)  # HashMap to store frequency of (nums[i] - i)
        good_pairs = 0

        for i, num in enumerate(nums):
            key = num - i  # Transformation nums[i] - i
            good_pairs += count_map[key]  # Count how many times we've seen this value
            count_map[key] += 1  # Update frequency

        return total_pairs - good_pairs  # Compute bad pairs
