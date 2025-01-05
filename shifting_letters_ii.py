class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        shift_accumulation = [0] * (n + 1)  # Using extra space for easier range manipulation
        
        # Apply the difference array technique for shifts
        for start, end, direction in shifts:
            if direction == 1:  # Forward shift
                shift_accumulation[start] += 1
                shift_accumulation[end + 1] -= 1
            else:  # Backward shift
                shift_accumulation[start] -= 1
                shift_accumulation[end + 1] += 1
        
        # Apply the accumulated shifts
        current_shift = 0
        result = []
        
        for i in range(n):
            current_shift += shift_accumulation[i]
            # Apply the shift considering the circular nature of the alphabet
            new_char = chr((ord(s[i]) - ord('a') + current_shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)


# Example usage:
solution = Solution()

# Test Case 1
s1 = "abc"
shifts1 = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
print(solution.shiftingLetters(s1, shifts1))  # Output: "ace"

# Test Case 2
s2 = "dztz"
shifts2 = [[0, 0, 0], [1, 1, 1]]
print(solution.shiftingLetters(s2, shifts2))  # Output: "catz"
