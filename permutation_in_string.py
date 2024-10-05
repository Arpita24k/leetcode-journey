class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        
        count_s1 = Counter(s1)
        window = Counter(s2[:len1])
        
        if window == count_s1:
            return True
        
        for i in range(len1, len2):
            window[s2[i]] += 1
            window[s2[i - len1]] -= 1
            if window[s2[i - len1]] == 0:
                del window[s2[i - len1]]
            if window == count_s1:
                return True
        
        return False

# Example usage for checkInclusion:
solution = Solution()

# Testcase for checkInclusion
s1 = "ab"
s2 = "eidbaooo"
print(f"Output: {solution.checkInclusion(s1, s2)}")  # Expected Output: True



