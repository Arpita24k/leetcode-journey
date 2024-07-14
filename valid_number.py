class Solution:
    def isNumber(self, s: str) -> bool:
        """
        Function to determine if the input string is a valid number.
        
        Args:
        s: Input string.
        
        Returns:
        Boolean value indicating whether the string is a valid number.
        """
        def is_integer(part):
            # Check if the part is a valid integer
            if not part:  # Empty part is not valid
                return False
            if part[0] in "+-":  # Remove leading sign
                part = part[1:]
            return part.isdigit()

        def is_decimal(part):
            # Check if the part is a valid decimal
            if not part:  # Empty part is not valid
                return False
            if part[0] in "+-":  # Remove leading sign
                part = part[1:]
            if '.' not in part:
                return False
            left, right = part.split('.', 1)
            if left == '' and right == '':  # At least one side must have digits
                return False
            if left and not left.isdigit():
                return False
            if right and not right.isdigit():
                return False
            return True
        
        s = s.strip()  # Remove leading and trailing spaces
        if not s:
            return False
        
        # Split the input string into base and exponent parts
        if 'e' in s or 'E' in s:
            parts = s.split('e') if 'e' in s else s.split('E')
            if len(parts) != 2:
                return False
            base, exp = parts
            return (is_integer(base) or is_decimal(base)) and is_integer(exp)
        
        return is_integer(s) or is_decimal(s)

# Example usage
solution = Solution()
print(solution.isNumber("0"))         # Output: True
print(solution.isNumber("e"))         # Output: False
print(solution.isNumber("."))         # Output: False
print(solution.isNumber("2e10"))      # Output: True
print(solution.isNumber("-90E3"))     # Output: True
print(solution.isNumber("99e2.5"))    # Output: False
print(solution.isNumber("--6"))       # Output: False
print(solution.isNumber("53.5e93"))   # Output: True
print(solution.isNumber("-123.456e789"))  # Output: True
