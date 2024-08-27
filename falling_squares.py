class Solution:
    def fallingSquares(self, positions):
        heights = []
        max_height = 0
        result = []
        
        for left, size in positions:
            right = left + size
            base_height = 0
            
            # Determine the maximum height the square can land on
            for i, (prev_left, prev_right, prev_height) in enumerate(heights):
                if prev_left < right and left < prev_right:  # Overlapping interval
                    base_height = max(base_height, prev_height)
            
            # The new height after placing the current square
            current_height = base_height + size
            heights.append((left, right, current_height))
            max_height = max(max_height, current_height)
            result.append(max_height)
        
        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    positions1 = [[1,2],[2,3],[6,1]]
    print(solution.fallingSquares(positions1))  # Output: [2, 5, 5]
    
    # Test Case 2
    positions2 = [[100,100],[200,100]]
    print(solution.fallingSquares(positions2))  # Output: [100, 100]
