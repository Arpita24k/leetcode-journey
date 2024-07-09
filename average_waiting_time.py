class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        current_time = 0
        total_waiting_time = 0
        
        for arrival, time in customers:
            # The chef starts preparing the order either when the customer arrives or when he finishes the previous order
            if current_time < arrival:
                current_time = arrival
            current_time += time
            total_waiting_time += current_time - arrival
        
        return total_waiting_time / len(customers)

# Example usage:
solution = Solution()

# Test cases
customers1 = [[1, 2], [2, 5], [4, 3]]
print(solution.averageWaitingTime(customers1))  # Output: 5.00000

customers2 = [[5, 2], [5, 4], [10, 3], [20, 1]]
print(solution.averageWaitingTime(customers2))  # Output: 3.25000
