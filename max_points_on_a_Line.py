class Solution:
    def maxPoints(self, points):
        import math
        from collections import defaultdict
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(points)
        if n < 3:
            return n
        
        max_points = 1
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicate = 1
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                
                g = gcd(dx, dy)
                slope = (dy // g, dx // g)
                slopes[slope] += 1
            
            current_max = duplicate
            for count in slopes.values():
                current_max = max(current_max, count + duplicate)
            
            max_points = max(max_points, current_max)
        
        return max_points

# Test the function with the provided examples
sol = Solution()
print(sol.maxPoints([[1, 1], [2, 2], [3, 3]]))  # Output: 3
print(sol.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))  # Output: 4
