from fractions import Fraction
import re
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Regular expression to find all fractions
        fractions = re.findall(r'[+-]?\d+/\d+', expression)
        
        # Initialize the result as 0/1 (a Fraction object)
        result = Fraction(0, 1)
        
        # Process each fraction in the expression
        for frac in fractions:
            result += Fraction(frac)
        
        # Convert the result back to the string in the required format
        return f"{result.numerator}/{result.denominator}"

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    expression1 = "-1/2+1/2"
    print(solution.fractionAddition(expression1))  # Output: "0/1"
    
    # Test Case 2
    expression2 = "-1/2+1/2+1/3"
    print(solution.fractionAddition(expression2))  # Output: "1/3"
    
    # Test Case 3
    expression3 = "1/3-1/2"
    print(solution.fractionAddition(expression3))  # Output: "-1/6"
