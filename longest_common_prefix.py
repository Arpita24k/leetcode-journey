from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Find the minimum length string in the list
        min_len_str = min(strs, key=len)
        
        for i, char in enumerate(min_len_str):
            for other_str in strs:
                if other_str[i] != char:
                    return min_len_str[:i]
        
        return min_len_str

# Example usage
solution = Solution()

strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]

print(solution.longestCommonPrefix(strs1))  # Output: "fl"
print(solution.longestCommonPrefix(strs2))  # Output: ""

