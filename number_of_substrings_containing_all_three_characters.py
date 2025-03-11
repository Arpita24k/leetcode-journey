from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        left = 0
        result = 0
        count = defaultdict(int)

        for right in range(n):
            count[s[right]] += 1
            
            # While the window contains at least one of each 'a', 'b', and 'c'
            while all(count[char] > 0 for char in 'abc'):
                # Every substring from current left to the end is valid
                result += n - right
                
                # Move the left pointer to reduce the window size
                count[s[left]] -= 1
                left += 1
        
        return result
