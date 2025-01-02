
#Count Vowel Strings in Ranges
class Solution:
    def vowelStrings(self, words, queries):
        """
        This function processes the queries and returns the result for each query.
        """
        vowels = set("aeiou")

        def is_valid(word):
            # Check if a word starts and ends with a vowel
            return word[0] in vowels and word[-1] in vowels

        # Build the prefix sum array
        n = len(words)
        prefix = [0] * n
        prefix[0] = 1 if is_valid(words[0]) else 0

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + (1 if is_valid(words[i]) else 0)

        # Process queries
        result = []
        for li, ri in queries:
            if li == 0:
                result.append(prefix[ri])
            else:
                result.append(prefix[ri] - prefix[li - 1])

        return result


