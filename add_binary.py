class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize pointers for both strings
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        
        # Loop through both strings from the end towards the beginning
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # Append the current bit to the result
            result.append(str(total % 2))
            # Update carry
            carry = total // 2
        
        # Since we added from the end, reverse the result to get the final answer
        return ''.join(result[::-1])

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    a1, b1 = "11", "1"
    a2, b2 = "1010", "1011"
    
    print(solution.addBinary(a1, b1))  # Output: "100"
    print(solution.addBinary(a2, b2))  # Output: "10101"
