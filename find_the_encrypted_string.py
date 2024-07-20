class Solution:
    def encryptString(self, s: str, k: int) -> str:
        n = len(s)
        # Initialize an empty list to store the encrypted characters
        encrypted_chars = [''] * n
        
        # Iterate over each character in the string
        for i in range(n):
            # Compute the new position using modulo to wrap around
            new_position = (i + k) % n
            # Place the character in the new position
            encrypted_chars[new_position] = s[i]
        
        # Join the list into a string and return
        return ''.join(encrypted_chars)

# Example usage:
solution = Solution()
print(solution.encryptString("dart", 3))  # Output: "tdar"
print(solution.encryptString("aaa", 1))   # Output: "aaa"
