class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        # Start with the first term
        current_sequence = "1"
        
        # Generate terms from 2 to n
        for _ in range(2, n + 1):
            next_sequence = ""
            i = 0
            while i < len(current_sequence):
                count = 1
                # Count consecutive identical characters
                while i + 1 < len(current_sequence) and current_sequence[i] == current_sequence[i + 1]:
                    i += 1
                    count += 1
                # Append the count and the character to the next sequence
                next_sequence += str(count) + current_sequence[i]
                i += 1
            current_sequence = next_sequence
        
        return current_sequence

# Example usage:
solution = Solution()

# Test cases
print(solution.countAndSay(1))  # Output: "1"
print(solution.countAndSay(4))  # Output: "1211"
print(solution.countAndSay(5))  # Output: "111221"
