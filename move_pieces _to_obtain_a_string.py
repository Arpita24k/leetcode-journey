class Solution:
    def canChange(self, start, target):
        """
        Check if target can be obtained from start by moving pieces 'L' and 'R'.

        Args:
        start (str): Starting configuration.
        target (str): Target configuration.

        Returns:
        bool: True if the target can be obtained, False otherwise.
        """
        # Remove underscores to compare relative order of 'L' and 'R'
        start_pieces = ''.join(c for c in start if c != '_')
        target_pieces = ''.join(c for c in target if c != '_')
        
        # If relative order of 'L' and 'R' doesn't match, return False
        if start_pieces != target_pieces:
            return False
        
        # Use two pointers to validate movement constraints
        i, j = 0, 0
        n = len(start)
        
        while i < n and j < n:
            # Skip underscores in both strings
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            
            # If both pointers reached the end, we're done
            if i == n and j == n:
                return True
            
            # If only one pointer reached the end, return False
            if i == n or j == n:
                return False
            
            # Validate movement constraints
            if start[i] != target[j]:
                return False
            if start[i] == 'L' and i < j:  # 'L' can't move right
                return False
            if start[i] == 'R' and i > j:  # 'R' can't move left
                return False
            
            # Move to the next piece
            i += 1
            j += 1
        
        return True
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    start1 = "_L__R__R_"
    target1 = "L______RR"
    print(solution.canChange(start1, target1))  # Output: True

    # Example 2
    start2 = "R_L_"
    target2 = "__LR"
    print(solution.canChange(start2, target2))  # Output: False

    # Example 3
    start3 = "_R"
    target3 = "R_"
    print(solution.canChange(start3, target3))  # Output: False
