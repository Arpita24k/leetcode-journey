class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 0, x
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # right will be the integer part of the square root

# Example usage:
solution = Solution()

# Test case 1:
x = 4
print(solution.mySqrt(x))  # Output: 2

# Test case 2:
x = 8
print(solution.mySqrt(x))  # Output: 2 (since the square root of 8 is around 2.828, we return the integer part)

# Test case 3:
x = 16
print(solution.mySqrt(x))  # Output: 4
