class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:
        def backtrack(start):
            if start in memo:  # Check if the result for this start index is already memoized
                return memo[start]  # Return the memoized result
            
            result = []  # Initialize the result list for this start index
            if start == len(s):  # If we have reached the end of the string
                result.append("")  # Add an empty string as a valid split
                return result  # Return the result list
            
            for end in range(start + 1, len(s) + 1):  # Iterate over all possible end indices
                word = s[start:end]  # Get the substring from start to end
                if word in wordDict:  # If the substring is a valid word in the dictionary
                    sublist = backtrack(end)  # Recursively get valid splits for the rest of the string
                    for sub in sublist:  # Iterate over all valid splits returned
                        if sub:  # If the split is not empty
                            result.append(word + " " + sub)  # Append the word followed by the split
                        else:
                            result.append(word)  # Append just the word if the split is empty
            
            memo[start] = result  # Memoize the result for this start index
            return result  # Return the result list

        wordDict = set(wordDict)  # Convert the word dictionary list to a set for O(1) look-up
        memo = {}  # Initialize the memoization dictionary
        return backtrack(0)  # Start the backtracking from index 0

# Example usage:
sol = Solution()
print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))  # Output: ["cats and dog", "cat sand dog"]
print(sol.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))  # Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: []
