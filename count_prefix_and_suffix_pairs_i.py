class Solution:
    def countPrefixSuffixPairs(self, words):
        """
        Count the number of index pairs (i, j) where words[i] is both a prefix and suffix of words[j].
        """
        # Helper function to check prefix and suffix condition
        def isPrefixAndSuffix(str1, str2):
            return str2.startswith(str1) and str2.endswith(str1)

        count = 0
        # Iterate through pairs (i, j) where i < j
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        
        return count


# Example Usage:
solution = Solution()

# Test Case 1
words1 = ["a", "aba", "ababa", "aa"]
print(solution.countPrefixSuffixPairs(words1))  # Output: 4

# Test Case 2
words2 = ["pa", "papa", "ma", "mama"]
print(solution.countPrefixSuffixPairs(words2))  # Output: 2

# Test Case 3
words3 = ["abab", "ab"]
print(solution.countPrefixSuffixPairs(words3))  # Output: 0
