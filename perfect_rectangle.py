class Solution:
    def isRectangleCover(self, rectangles):
        corner_set = set()  # Set to track corners
        total_area = 0  # Total area of all rectangles
        min_x = min_y = float('inf')  # Initialize min bounds
        max_x = max_y = float('-inf')  # Initialize max bounds
        
        # Iterate through each rectangle
        for x1, y1, x2, y2 in rectangles:
            # Calculate the area of the current rectangle and add to total area
            total_area += (x2 - x1) * (y2 - y1)
            # Update the bounding box
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            
            # List of the four corners of the current rectangle
            corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
            
            # Update the corner set for the current rectangle
            for corner in corners:
                if corner in corner_set:
                    corner_set.remove(corner)  # Remove if already exists (shared boundary)
                else:
                    corner_set.add(corner)  # Add if does not exist

        # Calculate the area of the bounding rectangle
        bounding_area = (max_x - min_x) * (max_y - min_y)
        
        # Check if total area of rectangles matches the bounding area
        if total_area != bounding_area:
            return False
        
        # Check if the corner set has exactly 4 corners
        if len(corner_set) != 4:
            return False
        
        # Expected corners of the bounding rectangle
        expected_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        
        # Check if the corners match the expected corners
        return corner_set == expected_corners

# Example usage
solution = Solution()
rectangles1 = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
rectangles2 = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
rectangles3 = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]

print(solution.isRectangleCover(rectangles1))  # Output: True
print(solution.isRectangleCover(rectangles2))  # Output: False
print(solution.isRectangleCover(rectangles3))  # Output: False
