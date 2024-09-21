class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result = []
        current = 1
        
        for _ in range(n):
            result.append(current)
            
            # Try to go to the next lexicographically smallest number
            if current * 10 <= n:
                current *= 10
            else:
                # If cannot multiply by 10, increment the current number
                if current >= n:
                    current //= 10
                
                current += 1
                
                # Handle cases where the current number ends in a 9 or overshoots
                while current % 10 == 0:
                    current //= 10
        
        return result

# Example usage:
solution = Solution()

# Example 1
n = 13
print(solution.lexicalOrder(n))  # Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 2
n = 2
print(solution.lexicalOrder(n))  # Output: [1, 2]
