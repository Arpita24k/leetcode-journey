class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix: int, n: int) -> int:
            """ Counts how many numbers are lexicographically between `prefix` and `prefix + 1` and <= n. """
            steps = 0
            first, last = prefix, prefix + 1
            while first <= n:
                steps += min(last, n + 1) - first
                first *= 10
                last *= 10
            return steps
        
        current = 1
        k -= 1  # Since we are starting from 1, we reduce k by 1
        
        while k > 0:
            steps = count_steps(current, n)
            
            if steps <= k:
                # Move to the next sibling
                current += 1
                k -= steps
            else:
                # Move to the next level (deeper in the subtree)
                current *= 10
                k -= 1
        
        return current

# Example usage:
solution = Solution()

# Example 1:
n = 13
k = 2
print(solution.findKthNumber(n, k))  # Output: 10

# Example 2:
n = 1
k = 1
print(solution.findKthNumber(n, k))  # Output: 1
