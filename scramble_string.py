class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        
        def _isScramble(s1, s2):
            if (s1, s2) in memo:
                return memo[(s1, s2)]
            
            if s1 == s2:
                return True
            
            if sorted(s1) != sorted(s2):
                return False
            
            n = len(s1)
            for i in range(1, n):
                # Check if s1[:i] matches s2[:i] and s1[i:] matches s2[i:]
                if _isScramble(s1[:i], s2[:i]) and _isScramble(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                # Check if s1[:i] matches s2[n-i:] and s1[i:] matches s2[:n-i]
                if _isScramble(s1[:i], s2[n-i:]) and _isScramble(s1[i:], s2[:n-i]):
                    memo[(s1, s2)] = True
                    return True
            
            memo[(s1, s2)] = False
            return False
        
        return _isScramble(s1, s2)

# Example usage:
solution = Solution()
print(solution.isScramble("great", "rgeat"))  # Output: True
print(solution.isScramble("abcde", "caebd"))  # Output: False
print(solution.isScramble("a", "a"))          # Output: True
