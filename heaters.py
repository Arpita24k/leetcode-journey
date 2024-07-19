import bisect

class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()
        min_radius = 0
        
        for house in houses:
            # Find the position to insert house in heaters to keep sorted order
            pos = bisect.bisect_left(heaters, house)
            
            # Calculate distances to the nearest heaters
            left_heater_dist = float('inf') if pos == 0 else house - heaters[pos - 1]
            right_heater_dist = float('inf') if pos == len(heaters) else heaters[pos] - house
            
            # Minimum distance to a heater for this house
            min_dist = min(left_heater_dist, right_heater_dist)
            
            # Update the minimum radius required
            min_radius = max(min_radius, min_dist)
        
        return min_radius

# Example usage:
solution = Solution()
print(solution.findRadius([1,2,3], [2]))  # Output: 1
print(solution.findRadius([1,2,3,4], [1,4]))  # Output: 1
print(solution.findRadius([1,5], [2]))  # Output: 3
