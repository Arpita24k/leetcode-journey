#fizz Buzz
class Solution:
    def fizzBuzz(self, n: int):
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    n = 3
    print("Input:", n)
    result = solution.fizzBuzz(n)
    print("Output:", result)  # Output should be ["1", "2", "Fizz"]

    # Test Case 2
    n = 5
    print("\nInput:", n)
    result = solution.fizzBuzz(n)
    print("Output:", result)  # Output should be ["1", "2", "Fizz", "4", "Buzz"]

    # Test Case 3
    n = 15
    print("\nInput:", n)
    result = solution.fizzBuzz(n)
    print("Output:", result)  # Output should be ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
