from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        Function to group anagrams together.
        
        Args:
        strs: List of strings.
        
        Returns:
        List of lists, where each sublist contains anagrams grouped together.
        """
        # Dictionary to hold lists of anagrams
        anagrams = defaultdict(list)
        
        # Iterate over each string in the input list
        for s in strs:
            # Sort the string and use it as a key
            key = tuple(sorted(s))
            # Append the original string to the corresponding list in the dictionary
            anagrams[key].append(s)
        
        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())

# Example usage
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
print(solution.groupAnagrams([""]))  # Output: [[""]]
print(solution.groupAnagrams(["a"]))  # Output: [["a"]]
