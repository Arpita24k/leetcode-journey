class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number into a list of digits
        digits = list(str(num))
        
        # Create an array to store the last occurrence of each digit (0-9)
        last = {int(d): i for i, d in enumerate(digits)}

        # Traverse through the digits
        for i, d in enumerate(digits):
            # Check if there's a larger digit in the future
            for larger_digit in range(9, int(d), -1):
                if last.get(larger_digit, -1) > i:
                    # Swap the current digit with the larger digit
                    digits[i], digits[last[larger_digit]] = digits[last[larger_digit]], digits[i]
                    # Return the number after swap
                    return int(''.join(digits))

        # If no swap occurred, return the original number
        return num

# Usage example:
solution = Solution()
print(solution.maximumSwap(2736))  # Output: 7236
print(solution.maximumSwap(9973))  # Output: 9973
