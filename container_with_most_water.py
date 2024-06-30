class Solution:
    def maxArea(self, height):
        # Initialize two pointers, one at the beginning and one at the end of the array
        left, right = 0, len(height) - 1
        # Variable to store the maximum area
        max_area = 0
        
        # Iterate while left pointer is less than right pointer
        while left < right:
            # Calculate the current area with the current left and right pointers
            current_area = min(height[left], height[right]) * (right - left)
            # Update max_area if current_area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer that points to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height2 = [1, 1]
    print(solution.maxArea(height1))  # Output: 49
    print(solution.maxArea(height2))  # Output: 1
