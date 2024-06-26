class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # Check the overall feasibility of completing the circuit
        if sum(gas) < sum(cost):
            return -1
        
        total_gas = 0
        start_station = 0
        current_balance = 0

        for i in range(len(gas)):
            current_balance += gas[i] - cost[i]
            # If balance is negative, reset start position and balance
            if current_balance < 0:
                start_station = i + 1
                current_balance = 0

        return start_station

# Example usage
solution = Solution()

# Test case 1
gas1 = [1, 2, 3, 4, 5]
cost1 = [3, 4, 5, 1, 2]
print(solution.canCompleteCircuit(gas1, cost1))  # Output: 3

# Test case 2
gas2 = [2, 3, 4]
cost2 = [3, 4, 3]
print(solution.canCompleteCircuit(gas2, cost2))  # Output: -1
