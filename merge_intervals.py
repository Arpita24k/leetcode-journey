from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals by the starting value
        intervals.sort(key=lambda x: x[0])

        merged_intervals = []
        for interval in intervals:
            # If the list of merged intervals is empty or if the current interval
            # does not overlap with the previous one, append it to the result.
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                # There is overlap, so merge the current interval with the previous one.
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals2 = [[1, 4], [4, 5]]
    
    print(solution.merge(intervals1))  # Output: [[1, 6], [8, 10], [15, 18]]
    print(solution.merge(intervals2))  # Output: [[1, 5]]
