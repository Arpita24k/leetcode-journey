class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        # Step 1: Calculate the total sum required
        m = len(rolls)
        total_sum = mean * (n + m)
        
        # Step 2: Calculate the sum of the known rolls
        sum_known_rolls = sum(rolls)
        
        # Step 3: Calculate the sum of the missing rolls
        missing_sum = total_sum - sum_known_rolls
        
        # Step 4: Check if the missing_sum can be distributed over n rolls
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        # Step 5: Distribute the missing_sum over n rolls
        result = [1] * n  # Start with all rolls being 1
        remaining_sum = missing_sum - n  # We've already assigned 1 to each roll
        
        # Distribute the remaining sum across the rolls
        for i in range(n):
            # We can add at most 5 to each roll (because it's already 1 and max is 6)
            addition = min(remaining_sum, 5)
            result[i] += addition
            remaining_sum -= addition
            if remaining_sum == 0:
                break
        
        return result

# Example usage:
solution = Solution()

# Test case 1:
rolls = [3, 2, 4, 3]
mean = 4
n = 2
print(solution.missingRolls(rolls, mean, n))  # Output: [6, 6]

# Test case 2:
rolls = [1, 5, 6]
mean = 3
n = 4
print(solution.missingRolls(rolls, mean, n))  # Output: [2, 3, 2, 2]

# Test case 3:
rolls = [1, 2, 3, 4]
mean = 6
n = 4
print(solution.missingRolls(rolls, mean, n))  # Output: []
