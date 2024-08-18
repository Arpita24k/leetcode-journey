class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1  # The first ugly number is 1

        i2 = i3 = i5 = 0  # Pointers for multiples of 2, 3, and 5
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        for i in range(1, n):
            dp[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            
            if dp[i] == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = dp[i2] * 2
            
            if dp[i] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = dp[i3] * 3
            
            if dp[i] == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = dp[i5] * 5

        return dp[-1]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    n = 10
    print(solution.nthUglyNumber(n))  # Output: 12
    
    # Test Case 2
    n = 1
    print(solution.nthUglyNumber(n))  # Output: 1
