#Minimum Number of Pushes to Type Word II
from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count frequency of each character
        char_frequency = Counter(word)

        # Step 2: Sort characters by frequency in descending order
        sorted_chars = sorted(char_frequency.items(), key=lambda item: item[1], reverse=True)

        # Step 3: Calculate the minimum number of key presses
        total_presses = 0
        current_key = 2
        current_key_presses = 1

        for char, frequency in sorted_chars:
            total_presses += frequency * current_key_presses
            current_key += 1
            if current_key > 9:
                current_key = 2
                current_key_presses += 1

        return total_presses

# Example usage
solution = Solution()
word1 = "abcde"
word2 = "xyzxyzxyzxyz"
word3 = "aabbccddeeffgghhiiiiii"

print(solution.minimumPushes(word1))  # Output: 5
print(solution.minimumPushes(word2))  # Output: 12
print(solution.minimumPushes(word3))  # Output: 24
