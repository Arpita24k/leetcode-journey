class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        # Calculate the total chalk used in one complete round
        total_chalk = sum(chalk)
        
        # Reduce k modulo the total chalk used in one complete round
        k %= total_chalk
        
        # Iterate through the students to find who will run out of chalk
        for i in range(len(chalk)):
            # If the current student's chalk usage exceeds the remaining k, return their index
            if chalk[i] > k:
                return i
            # Subtract the current student's chalk usage from k
            k -= chalk[i]

        # The problem guarantees that a solution always exists, so we never reach this point
        return -1

# Example usage:
chalk = [5, 1, 5]
k = 22
solution = Solution()
print(solution.chalkReplacer(chalk, k))  # Output: 0
