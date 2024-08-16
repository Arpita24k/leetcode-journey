class Solution:
    def maxDistance(self, arrays):
        # Initialize the global minimum and maximum values with the first array's elements
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        max_distance = 0
        
        # Iterate through the remaining arrays
        for i in range(1, len(arrays)):
            current_array = arrays[i]
            
            # Calculate potential max distances using the current array
            potential_max_distance_1 = abs(current_array[-1] - min_val)
            potential_max_distance_2 = abs(max_val - current_array[0])
            
            # Update the maximum distance encountered so far
            max_distance = max(max_distance, potential_max_distance_1, potential_max_distance_2)
            
            # Update the global min and max with the current array's first and last elements
            min_val = min(min_val, current_array[0])
            max_val = max(max_val, current_array[-1])
        
        return max_distance

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    arrays1 = [[1,2,3],[4,5],[1,2,3]]
    print(solution.maxDistance(arrays1))  # Output: 4

    # Test Case 2
    arrays2 = [[1],[1]]
    print(solution.maxDistance(arrays2))  # Output: 0
