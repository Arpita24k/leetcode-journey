class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        
        result = []
        
        # Determine the sign of the result
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        # Work with absolute values for simplicity
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Add the integral part
        integral_part = numerator // denominator
        result.append(str(integral_part))
        
        # Calculate the remainder
        remainder = numerator % denominator
        
        # If there is no remainder, return the result
        if remainder == 0:
            return "".join(result)
        
        # Otherwise, process the fractional part
        result.append(".")
        remainders = {}
        
        while remainder != 0:
            # If the remainder is already seen, we have a repeating sequence
            if remainder in remainders:
                result.insert(remainders[remainder], "(")
                result.append(")")
                break
            
            # Remember the position where this remainder first appeared
            remainders[remainder] = len(result)
            
            # Generate the next digit
            remainder *= 10
            next_digit = remainder // denominator
            result.append(str(next_digit))
            
            # Update remainder
            remainder %= denominator
        
        return "".join(result)

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    print(solution.fractionToDecimal(1, 2))  # Output: "0.5"
    
    # Test Case 2
    print(solution.fractionToDecimal(2, 1))  # Output: "2"
    
    # Test Case 3
    print(solution.fractionToDecimal(4, 333))  # Output: "0.(012)"
