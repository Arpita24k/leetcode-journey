from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums):
        
        product_count = defaultdict(int)
        n = len(nums)

        # Compute all pair products and count occurrences
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        # Compute valid tuples
        result = 0
        for freq in product_count.values():
            if freq > 1:
                result += (freq * (freq - 1) // 2) * 8  # Choose 2 pairs * 8 permutations

        return result
