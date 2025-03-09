class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        n = len(colors)
        extended_colors = colors + colors[:k-1]  # Handle circular case
        
        count = 0
        for i in range(n):  # Only iterate over original indices
            valid = True
            for j in range(1, k):  # Check the alternating pattern
                if extended_colors[i + j] == extended_colors[i + j - 1]:
                    valid = False
                    break
            if valid:
                count += 1
        
        return count

# Example Test Case
solution = Solution()
print(solution.numberOfAlternatingGroups([0,1,0,1,0], 3))  # Output: 3
