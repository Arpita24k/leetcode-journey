# Integer to English Words
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        # Define the words for numbers
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return less_than_20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + helper(num % 10)
            else:
                return less_than_20[num // 100] + " Hundred " + helper(num % 100)
        
        res = ""
        for i, word in enumerate(thousands):
            if num % 1000 != 0:
                res = helper(num % 1000) + word + " " + res
            num //= 1000
        
        return res.strip()

# Example usage
solution = Solution()
print(solution.numberToWords(123))        # Output: "One Hundred Twenty Three"
print(solution.numberToWords(12345))      # Output: "Twelve Thousand Three Hundred Forty Five"
print(solution.numberToWords(1234567))    # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
print(solution.numberToWords(0))          # Output: "Zero"
