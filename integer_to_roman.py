
class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the mappings from integer values to Roman numeral strings
        value_to_roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        # Initialize the result string
        roman = ""
        
        # Iterate over the mappings
        for value, symbol in value_to_roman:
            # Append the Roman numeral symbol while subtracting its value from num
            while num >= value:
                roman += symbol
                num -= value
        
        return roman

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(3749))  # Output: "MMMDCCXLIX"
    print(solution.intToRoman(58))    # Output: "LVIII"
    print(solution.intToRoman(1994))  # Output: "MCMXCIV"
