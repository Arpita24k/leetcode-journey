class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        # Initialize the variables
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0

        # Traverse through each price in the prices array
        for price in prices:
            # For the first transaction
            buy1 = max(buy1, -price)      # Max profit after buying the first stock
            sell1 = max(sell1, buy1 + price)  # Max profit after selling the first stock

            # For the second transaction
            buy2 = max(buy2, sell1 - price)  # Max profit after buying the second stock
            sell2 = max(sell2, buy2 + price)  # Max profit after selling the second stock

        # The result is the maximum profit from two transactions
        return sell2
