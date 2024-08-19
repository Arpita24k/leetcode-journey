class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1
        while factor <= n:
            lower = n - (n // factor) * factor
            current_digit = (n // factor) % 10
            higher = n // (factor * 10)
            
            # Counting digit '1's contributed by the current digit place
            if current_digit == 0:
                count += higher * factor
            elif current_digit == 1:
                count += higher * factor + lower + 1
            else:
                count += (higher + 1) * factor
                
            factor *= 10
        
        return count

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    n1 = 13
    print(solution.countDigitOne(n1))  # Output: 6
    
    # Test Case 2
    n2 = 0
    print(solution.countDigitOne(n2))  # Output: 0
    
    # Test Case 3
    n3 = 314
    print(solution.countDigitOne(n3))  # Example given earlier
