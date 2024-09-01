from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if it's possible to form a 2D array with the given dimensions
        if len(original) != m * n:
            return []
        
        # Create the 2D array
        result = []
        for i in range(m):
            # Slice out the subarray for each row
            result.append(original[i * n:(i + 1) * n])
        
        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    original1 = [1, 2, 3, 4]
    m1, n1 = 2, 2
    print(solution.construct2DArray(original1, m1, n1))  # Output: [[1, 2], [3, 4]]
    
    # Test Case 2
    original2 = [1, 2, 3]
    m2, n2 = 1, 3
    print(solution.construct2DArray(original2, m2, n2))  # Output: [[1, 2, 3]]
    
    # Test Case 3
    original3 = [1, 2]
    m3, n3 = 1, 1
    print(solution.construct2DArray(original3, m3, n3))  # Output: []
