class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case for zero multiplication
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array with zeros
        result = [0] * (len(num1) + len(num2))
        
        # Reverse both numbers to facilitate multiplication from least significant digit
        num1, num2 = num1[::-1], num2[::-1]
        
        # Multiply each digit and add to result
        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j])
                result[i + j] += product
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # Remove leading zeros and convert result back to string
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        return ''.join(map(str, result[::-1]))

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    num1 = "123"
    num2 = "456"
    
    print(solution.multiply(num1, num2))  # Output: "56088"
    
    num1 = "2"
    num2 = "3"
    
    print(solution.multiply(num1, num2))  # Output: "6"
