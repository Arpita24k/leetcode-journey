class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = ""
        n = len(s)

        # Iterate through the string in chunks of size k
        for i in range(0, n, k):
            substring = s[i:i + k]
            hash_sum = sum(ord(char) - ord('a') for char in substring)  # Sum of hash values
            hashed_char = chr((hash_sum % 26) + ord('a'))  # Convert to the corresponding character
            result += hashed_char  # Append to result
        
        return result

# Example usage:
sol = Solution()

# Example 1:
s1 = "abcd"
k1 = 2
print(sol.stringHash(s1, k1))  # Output: "bf"

# Example 2:
s2 = "mxz"
k2 = 3
print(sol.stringHash(s2, k2))  # Output: "i"
