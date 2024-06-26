class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Split the string into words
        if len(pattern) != len(words):  # Check if the number of words matches the pattern length
            return False

        # Create dictionaries to store mappings between pattern characters and words
        pattern_to_word = {}
        word_to_pattern = {}

        for p, w in zip(pattern, words):
            if p in pattern_to_word:
                if pattern_to_word[p] != w:  # Mismatch in pattern to word mapping
                    return False
            else:
                pattern_to_word[p] = w

            if w in word_to_pattern:
                if word_to_pattern[w] != p:  # Mismatch in word to pattern mapping
                    return False
            else:
                word_to_pattern[w] = p

        return True

# Example usage:
solution = Solution()

print(solution.wordPattern("abba", "dog cat cat dog"))      # Output: True
print(solution.wordPattern("abba", "dog cat cat fish"))     # Output: False
print(solution.wordPattern("aaaa", "dog cat cat dog"))      # Output: False
print(solution.wordPattern("abba", "dog dog dog dog"))      # Output: False
