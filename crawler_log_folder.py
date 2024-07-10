from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0  # Initialize depth to represent the current folder level
        
        for log in logs:
            if log == "../":  # Move to the parent folder
                if depth > 0:
                    depth -= 1  # Decrease depth if not already at the main folder
            elif log == "./":  # Stay in the same folder
                continue
            else:  # Move to a child folder
                depth += 1  # Increase depth
        
        return depth  # Return the current depth, which is the number of steps back to main folder

# Example usage:
solution = Solution()

# Test cases
logs1 = ["d1/","d2/","../","d21/","./"]
print(solution.minOperations(logs1))  # Output: 2

logs2 = ["d1/","d2/","./","d3/","../","d31/"]
print(solution.minOperations(logs2))  # Output: 3

logs3 = ["d1/","../","../","../"]
print(solution.minOperations(logs3))  # Output: 0
