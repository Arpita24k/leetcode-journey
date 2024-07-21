import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # List of factorial values
        factorial = [1] * (n + 1)
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
        
        # List of numbers to get the permutation from
        numbers = [str(i) for i in range(1, n + 1)]
        # Result permutation
        result = []
        
        # Convert k to 0-based index
        k -= 1
        
        for i in range(n, 0, -1):
            # Determine the current position digit
            index = k // factorial[i - 1]
            result.append(numbers[index])
            # Remove used number
            numbers.pop(index)
            # Update k
            k %= factorial[i - 1]
        
        return ''.join(result)

# Examples
solution = Solution()
print(solution.getPermutation(3, 3))  # Output: "213"
print(solution.getPermutation(4, 9))  # Output: "2314"
print(solution.getPermutation(3, 1))  # Output: "123"
