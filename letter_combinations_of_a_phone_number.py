class Solution:
    def letterCombinations(self, digits: str):
        """
        Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
        that the number could represent. Return the answer in any order.
        
        Parameters:
        digits (str): A string containing digits from 2-9 inclusive.

        Returns:
        List[str]: A list of all possible letter combinations.
        """
        if not digits:
            return []

        # Mapping of digit to letters, similar to the telephone buttons
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(index, path):
            """
            Helper function to perform backtracking.

            Parameters:
            index (int): The current index in the digits string.
            path (str): The current combination of letters being formed.
            """
            # If the current path length is equal to the digits length, we have a complete combination
            if index == len(digits):
                combinations.append(path)
                return

            # Get the letters corresponding to the current digit
            possible_letters = phone_map[digits[index]]

            # Iterate over each letter and recurse
            for letter in possible_letters:
                backtrack(index + 1, path + letter)

        # List to hold the final combinations
        combinations = []

        # Start backtracking from index 0 and an empty path
        backtrack(0, "")

        return combinations

# Example usage:
solution = Solution()

# Example 1
print(solution.letterCombinations("23"))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2
print(solution.letterCombinations(""))    # Output: []

# Example 3
print(solution.letterCombinations("2"))   # Output: ["a","b","c"]
