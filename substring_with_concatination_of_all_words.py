from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []  # Return an empty list if input string or words list is empty
        
        word_len = len(words[0])  # Length of each word in words
        total_len = word_len * len(words)  # Total length of all words concatenated
        word_count = Counter(words)  # Frequency map of words
        
        result = []  # List to store starting indices of valid substrings
        
        # Iterate over each possible starting index in s where a concatenated substring could start
        for i in range(len(s) - total_len + 1):
            substring = s[i:i + total_len]  # Extract substring of total_len from current index i
            # Divide the substring into words of length word_len
            words_in_substring = [
                substring[j:j + word_len]
                for j in range(0, total_len, word_len)
            ]
            # Compare frequency map of words in the substring with the original word_count
            if Counter(words_in_substring) == word_count:
                result.append(i)  # If they match, add the starting index to the result list
        
        return result  # Return the list of starting indices

# Example usage:
solution = Solution()

# Test cases
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print(solution.findSubstring(s1, words1))  # Output: [0, 9]

s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print(solution.findSubstring(s2, words2))  # Output: []

s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
print(solution.findSubstring(s3, words3))  # Output: [6, 9, 12]
