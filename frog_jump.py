class Solution:
    def canCross(self, stones):
        # Helper function for DFS with memoization
        def dfs(position, last_jump):
            # If we reached the last stone, return True
            if position == stones[-1]:
                return True
            # Memoization key
            key = (position, last_jump)
            if key in memo:
                return memo[key]
            
            # Explore all possible jumps
            for jump in [last_jump - 1, last_jump, last_jump + 1]:
                if jump > 0 and position + jump in stone_positions:
                    if dfs(position + jump, jump):
                        memo[key] = True
                        return True
            
            memo[key] = False
            return False
        
        # Set to store stone positions for quick lookup
        stone_positions = set(stones)
        # Dictionary for memoization
        memo = {}
        
        # Start DFS from the first stone with an initial jump of 1
        return dfs(stones[0], 0)

# Example usage
solution = Solution()
stones1 = [0, 1, 3, 5, 6, 8, 12, 17]
stones2 = [0, 1, 2, 3, 4, 8, 9, 11]

print(solution.canCross(stones1))  # Output: true
print(solution.canCross(stones2))  # Output: false
