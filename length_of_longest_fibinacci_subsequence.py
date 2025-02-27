from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr):
        """
        Returns the length of the longest Fibonacci-like subsequence.

        Args:
        arr (List[int]): Strictly increasing list of integers.

        Returns:
        int: Length of the longest Fibonacci-like subsequence.
        """
        index_map = {num: i for i, num in enumerate(arr)}
        dp = defaultdict(lambda: 2)  # Default Fibonacci sequence length is at least 2
        max_length = 0

        # Iterate over all pairs (i, j) where i < j
        for j in range(len(arr)):
            for i in range(j):
                # Calculate the previous number needed in Fibonacci sequence
                prev_num = arr[j] - arr[i]
                if prev_num in index_map and index_map[prev_num] < i:
                    k = index_map[prev_num]  # Previous number index
                    dp[(i, j)] = dp[(k, i)] + 1  # Extend Fibonacci-like sequence
                    max_length = max(max_length, dp[(i, j)])

        return max_length if max_length >= 3 else 0
