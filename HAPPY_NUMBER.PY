class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit = number % 10
                total_sum += digit * digit
                number //= 10
            return total_sum
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    n1 = 19
    print(solution.isHappy(n1))  # Output: True
    
    # Test Case 2
    n2 = 2
    print(solution.isHappy(n2))  # Output: False
