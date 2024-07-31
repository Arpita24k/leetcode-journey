class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # Initialize an empty stack
        max_area = 0  # Variable to store the maximum area
        index = 0  # Start from the first bar
        
        while index < len(heights):
            # If stack is empty or the current bar is higher than the bar at the top of the stack
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)  # Push the current index to the stack
                index += 1  # Move to the next bar
            else:
                # Pop the top of the stack and calculate the area
                top_of_stack = stack.pop()
                height = heights[top_of_stack]
                # Calculate the width
                width = index if not stack else index - stack[-1] - 1
                # Update the maximum area
                max_area = max(max_area, height * width)
        
        # Process remaining bars in stack
        while stack:
            top_of_stack = stack.pop()
            height = heights[top_of_stack]
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area

# Example usage:
sol = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # Output: 10
print(sol.largestRectangleArea([2, 4]))  # Output: 4
