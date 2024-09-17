from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        # Step 1: Split both sentences into words
        words1 = s1.split()
        words2 = s2.split()
        
        # Step 2: Count the occurrences of each word in both sentences
        word_count = Counter(words1) + Counter(words2)
        
        # Step 3: Return words that appear exactly once in total
        return [word for word, count in word_count.items() if count == 1]

# Example usage:
solution = Solution()

# Example 1:
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(solution.uncommonFromSentences(s1, s2))  # Output: ["sweet", "sour"]

# Example 2:
s1 = "apple apple"
s2 = "banana"
print(solution.uncommonFromSentences(s1, s2))  # Output: ["banana"]
