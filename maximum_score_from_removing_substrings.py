class Solution:
    def maximum_gain(self, s: str, x: int, y: int) -> int:
        def remove_and_score(s, first, second, score):
            stack = []
            total_score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()  # Remove the matching first character
                    total_score += score  # Add the score for the removed substring
                else:
                    stack.append(char)  # Add current character to stack
            return "".join(stack), total_score
        
        if x > y:
            # Prioritize removing "ab"
            s, score1 = remove_and_score(s, 'a', 'b', x)
            s, score2 = remove_and_score(s, 'b', 'a', y)
        else:
            # Prioritize removing "ba"
            s, score1 = remove_and_score(s, 'b', 'a', y)
            s, score2 = remove_and_score(s, 'a', 'b', x)
        
        return score1 + score2

    # Alias for compatibility with test environments that use camelCase
    maximumGain = maximum_gain

# Example 1
s1 = "cdbcbbaaabab"
x1 = 4
y1 = 5
solution = Solution()
print(solution.maximum_gain(s1, x1, y1))  # Output: 19

# Example 2
s2 = "aabbaaxybbaabb"
x2 = 5
y2 = 4
print(solution.maximum_gain(s2, x2, y2))  # Output: 20
