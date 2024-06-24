import bisect

class Solution:
    def preprocess(self, t: str):
        from collections import defaultdict
        char_indices = defaultdict(list)
        for index, char in enumerate(t):
            char_indices[char].append(index)
        return char_indices
    
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        char_indices = self.preprocess(t)
        current_position = -1
        
        for char in s:
            if char not in char_indices:
                return False
            
            indices = char_indices[char]
            i = bisect.bisect_right(indices, current_position)
            
            if i == len(indices):
                return False
            
            current_position = indices[i]
        
        return True

# Example usage
s1 = "abc"
t1 = "ahbgdc"
print(Solution().isSubsequence(s1, t1))  # Output: True

s2 = "axc"
t2 = "ahbgdc"
print(Solution().isSubsequence(s2, t2))  # Output: False
