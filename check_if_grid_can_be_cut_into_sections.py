class Solution:
    def checkValidCuts(self, n, rectangles):
        def check(axis):
            # Project onto the selected axis (x or y)
            intervals = []
            for r in rectangles:
                if axis == 0:  # Vertical cuts -> x-axis
                    intervals.append((r[0], r[2]))
                else:  # Horizontal cuts -> y-axis
                    intervals.append((r[1], r[3]))
            
            # Sort intervals by start
            intervals.sort()
            m = len(intervals)
            
            # Sweep once and group non-overlapping intervals
            groups = []
            curr_start, curr_end = intervals[0]
            for i in range(1, m):
                start, end = intervals[i]
                if start >= curr_end:
                    groups.append((curr_start, curr_end))
                    curr_start, curr_end = start, end
                else:
                    curr_end = max(curr_end, end)
            groups.append((curr_start, curr_end))
            
            # If we have at least 3 non-overlapping groups, we can place 2 cuts between them
            return len(groups) >= 3
        
        # Try vertical and horizontal axis
        return check(0) or check(1)
