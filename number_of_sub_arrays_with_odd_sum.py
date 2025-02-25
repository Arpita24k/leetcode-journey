class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        odd_count, even_count = 0, 1  # Initial even count for prefix sum = 0
        prefix_sum, result = 0, 0

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 1:  # Odd prefix sum
                result = (result + even_count) % MOD
                odd_count += 1
            else:  # Even prefix sum
                result = (result + odd_count) % MOD
                even_count += 1

        return result
