class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        current_product = x
        
        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2
        
        return result

# Examples
solution = Solution()
print(solution.myPow(2.00000, 10))  # Output: 1024.00000
print(solution.myPow(2.10000, 3))   # Output: 9.26100
print(solution.myPow(2.00000, -2))  # Output: 0.25000
