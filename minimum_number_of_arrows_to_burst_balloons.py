class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # Sort the balloons by their end points
        points.sort(key=lambda x: x[1])
        
        arrows = 1  # We need at least one arrow
        current_end = points[0][1]  # Shoot the first arrow at the end of the first balloon
        
        for i in range(1, len(points)):
            if points[i][0] > current_end:  # A new arrow is needed
                arrows += 1
                current_end = points[i][1]  # Update the position of the current arrow
        
        return arrows

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    points1 = [[10,16],[2,8],[1,6],[7,12]]
    print(solution.findMinArrowShots(points1))  # Output: 2
    
    # Test Case 2
    points2 = [[1,2],[3,4],[5,6],[7,8]]
    print(solution.findMinArrowShots(points2))  # Output: 4
    
    # Test Case 3
    points3 = [[1,2],[2,3],[3,4],[4,5]]
    print(solution.findMinArrowShots(points3))  # Output: 2
