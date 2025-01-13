class Solution:
    def mincostTickets(self, days, costs):
        # Create a set for fast lookup of travel days
        travel_days = set(days)
        dp = [0] * (366)  # Day 0 to Day 365

        # Fill the dp array
        for day in range(1, 366):
            if day not in travel_days:
                dp[day] = dp[day - 1]  # No travel, carry forward the cost
            else:
                dp[day] = min(
                    dp[day - 1] + costs[0],  # 1-day pass
                    dp[max(0, day - 7)] + costs[1],  # 7-day pass
                    dp[max(0, day - 30)] + costs[2]  # 30-day pass
                )
        
        # Return the final cost for the last day of travel
        return dp[365]

# ✅ Example Usage
solution = Solution()

# Test Case 1
days1 = [1,4,6,7,8,20]
costs1 = [2,7,15]
print(solution.mincostTickets(days1, costs1))  # Output: 11

# Test Case 2
days2 = [1,2,3,4,5,6,7,8,9,10,30,31]
costs2 = [2,7,15]
print(solution.mincostTickets(days2, costs2))  # Output: 17
