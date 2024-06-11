from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]  # Reverse the digits to make it easier to handle the carry
        carry, i = 1, 0
        
        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(1)  # Append 1 if we are out of bounds and need to add a new digit
                carry = 0
                
            i += 1
        
        result = digits[::-1]  # Reverse the digits back to the original order
        print("Output:", result)
        return result

# Example usage
solution = Solution()
digits = [1, 2, 3]
solution.plusOne(digits)
