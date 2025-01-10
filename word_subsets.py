from collections import Counter

class Solution:
    def wordSubsets(self, words1, words2):
        # Step 1: Calculate the maximum frequency of each letter required in words2
        max_freq = Counter()
        for word in words2:
            freq = Counter(word)
            for char in freq:
                max_freq[char] = max(max_freq[char], freq[char])

        # Step 2: Check if each word in words1 meets the requirement
        universal_words = []
        for word in words1:
            word_freq = Counter(word)
            # Check if word_freq satisfies all constraints in max_freq
            if all(word_freq[char] >= max_freq[char] for char in max_freq):
                universal_words.append(word)
        
        return universal_words

# Example Usage:
solution = Solution()
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]
print(solution.wordSubsets(words1, words2))  # Output: ["facebook","google","leetcode"]

words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["l", "e"]
print(solution.wordSubsets(words1, words2))  # Output: ["apple","google","leetcode"]
