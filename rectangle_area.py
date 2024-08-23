class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Area of the first rectangle
        area1 = (ax2 - ax1) * (ay2 - ay1)
        
        # Area of the second rectangle
        area2 = (bx2 - bx1) * (by2 - by1)
        
        # Calculate the overlap
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        
        # Area of the overlapping region
        overlap_area = overlap_width * overlap_height
        
        # Total area covered by the two rectangles
        return area1 + area2 - overlap_area

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    ax1, ay1, ax2, ay2 = -3, 0, 3, 4
    bx1, by1, bx2, by2 = 0, -1, 9, 2
    print(solution.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))  # Output: 45
    
    # Test Case 2
    ax1, ay1, ax2, ay2 = -2, -2, 2, 2
    bx1, by1, bx2, by2 = -2, -2, 2, 2
    print(solution.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))  # Output: 16
