class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Step 1: Count total number of 'a' characters in the string
        total_a = s.count('a')
        # Step 2: Initialize the variables
        min_deletions = float('inf')
        b_count = 0  # Count of 'b' characters encountered so far
        
        # Step 3: Iterate through each character in the string
        for char in s:
            if char == 'a':
                # Decrement the count of 'a' remaining to the right
                total_a -= 1
            else:
                # Increment the count of 'b' encountered so far
                b_count += 1
            
            # Calculate minimum deletions required to keep the string balanced
            min_deletions = min(min_deletions, b_count + total_a)
        
        # Step 4: The minimum deletions also consider deleting all 'a's if needed
        return min(min_deletions, b_count)

# Example usage:
sol = Solution()
print(sol.minimumDeletions("aababbab"))  # Output: 2
print(sol.minimumDeletions("bbaaaaabb"))  # Output: 2
