class Solution:
    def prefixCount(self, words, pref):
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count

# Example Usage
solution = Solution()
words1 = ["pay", "attention", "practice", "attend"]
pref1 = "at"
print(solution.prefixCount(words1, pref1))  # Output: 2

words2 = ["leetcode", "win", "loops", "success"]
pref2 = "code"
print(solution.prefixCount(words2, pref2))  # Output: 0
