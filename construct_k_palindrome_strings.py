from collections import Counter

class Solution:
    def canConstruct(self, s, k):
        # If k exceeds the string length, it's impossible
        if k > len(s):
            return False
        
        # Count frequency of each character
        freq = Counter(s)
        
        # Count characters with odd frequency
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        
        # Check if the number of odd characters fits into the k partitions
        return odd_count <= k

# Example Usage:
solution = Solution()

# Test Case 1
s1, k1 = "annabelle", 2
print(solution.canConstruct(s1, k1))  # Output: True

# Test Case 2
s2, k2 = "leetcode", 3
print(solution.canConstruct(s2, k2))  # Output: False

# Test Case 3
s3, k3 = "true", 4
print(solution.canConstruct(s3, k3))  # Output: True
