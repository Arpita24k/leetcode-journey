from collections import defaultdict
import functools

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        
        # Create a dictionary to store the positions of each character in the ring
        char_pos = defaultdict(list)
        for i, c in enumerate(ring):
            char_pos[c].append(i)
        
        # Memoization decorator for the recursive function
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m:
                return 0
            
            res = float('inf')
            for k in char_pos[key[i]]:
                # Calculate the distance between current position j and next position k
                dist = min((k - j) % n, (j - k) % n)
                res = min(res, dist + dfs(i + 1, k) + 1)
            
            return res
        
        return dfs(0, 0)

# Examples
solution = Solution()
print(solution.findRotateSteps("godding", "gd"))       # Output: 4
print(solution.findRotateSteps("godding", "godding"))  # Output: 13
