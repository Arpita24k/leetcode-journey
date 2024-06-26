class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # Sort the citations in non-increasing order
        citations.sort(reverse=True)
        
        h_index = 0
        # Loop through the sorted list and find the h-index
        for i, c in enumerate(citations):
            if c >= i + 1:
                h_index = i + 1
            else:
                break
        
        return h_index

# Example usage
solution = Solution()

# Test case 1
citations1 = [3, 0, 6, 1, 5]
print(solution.hIndex(citations1))  # Output: 3

# Test case 2
citations2 = [1, 3, 1]
print(solution.hIndex(citations2))  # Output: 1
