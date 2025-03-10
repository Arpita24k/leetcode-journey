from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        result = 0
        
        # Iterate through each possible starting index
        for start in range(n):
            vowel_count = defaultdict(int)
            consonant_count = 0
            
            # Expand the substring from start to end
            for end in range(start, n):
                char = word[end]
                
                if char in vowels:
                    vowel_count[char] += 1
                else:
                    consonant_count += 1
                
                # Check if the current substring is valid
                if len(vowel_count) == 5 and consonant_count == k:
                    result += 1
                # Stop expanding if we have too many consonants
                if consonant_count > k:
                    break
        
        return result

# Example Test Cases
solution = Solution()
print(solution.countOfSubstrings("aeioqq", 1))  # Output: 0
print(solution.countOfSubstrings("aeiou", 0))  # Output: 1
print(solution.countOfSubstrings("ieaouqqieaouqq", 1))  # Output: 3
