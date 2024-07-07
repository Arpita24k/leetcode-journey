class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = 0
        empty_bottles = 0

        while numBottles > 0:
            # Drink all full bottles
            total_drunk += numBottles
            empty_bottles += numBottles

            # Exchange empty bottles for full ones
            numBottles = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange

        return total_drunk

    def print_solution(self, numBottles: int, numExchange: int):
        result = self.numWaterBottles(numBottles, numExchange)
        print(f"Input: numBottles = {numBottles}, numExchange = {numExchange}")
        print(f"Output: {result}")

# Example usage:
solution = Solution()

# Example 1
solution.print_solution(9, 3)  # Output: 13

# Example 2
solution.print_solution(15, 4) # Output: 19
