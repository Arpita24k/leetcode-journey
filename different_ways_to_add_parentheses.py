class Solution:
    def diffWaysToCompute(self, expression):
        # Memoization dictionary to store results of sub-expressions
        memo = {}

        # Helper function to recursively compute different results
        def ways(expr):
            if expr in memo:
                return memo[expr]

            results = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    # Recursively calculate the left and right parts
                    left = ways(expr[:i])
                    right = ways(expr[i + 1:])

                    # Combine results of left and right based on the operator
                    for l in left:
                        for r in right:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            elif char == '*':
                                results.append(l * r)

            # If there are no operators in the expression, it's a single number
            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return ways(expression)

# Example usage
solution = Solution()

# Example 1
expression1 = "2-1-1"
print(solution.diffWaysToCompute(expression1))  # Output: [0, 2]

# Example 2
expression2 = "2*3-4*5"
print(solution.diffWaysToCompute(expression2))  # Output: [-34, -14, -10, -10, 10]
