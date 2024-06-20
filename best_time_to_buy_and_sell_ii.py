from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate the maximum profit obtained by buying and selling a stock multiple times.
        
        Args:
        - prices: List of stock prices on each day
        
        Returns:
        - Maximum profit
        """
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

# Example usage
solution = Solution()

prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [1, 2, 3, 4, 5]
prices3 = [7, 6, 4, 3, 1]

print("Max Profit for prices 1:", solution.maxProfit(prices1))  # Output: 7
print("Max Profit for prices 2:", solution.maxProfit(prices2))  # Output: 4
print("Max Profit for prices 3:", solution.maxProfit(prices3))  # Output: 0
