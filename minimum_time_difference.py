class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        # Step 1: Convert time points to minutes
        def timeToMinutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        # Step 2: Convert all time points to minutes and sort them
        minutes = sorted(timeToMinutes(time) for time in timePoints)
        
        # Step 3: Initialize the minimum difference to be large
        min_diff = float('inf')
        
        # Step 4: Compute differences between consecutive time points
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        # Step 5: Also check the circular difference (last time point with first)
        min_diff = min(min_diff, 1440 + minutes[0] - minutes[-1])
        
        return min_diff

# Example usage:
solution = Solution()

# Example 1:
timePoints = ["23:59", "00:00"]
print(solution.findMinDifference(timePoints))  # Output: 1

# Example 2:
timePoints = ["00:00", "23:59", "00:00"]
print(solution.findMinDifference(timePoints))  # Output: 0
