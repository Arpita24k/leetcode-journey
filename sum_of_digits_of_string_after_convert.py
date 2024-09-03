class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert each character in s to its corresponding integer value
        num_str = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        # Step 2: Perform the sum of digits transformation k times
        for _ in range(k):
            num_str = str(sum(int(digit) for digit in num_str))
        
        return int(num_str)

# Example usage
s = "iiii"
k = 1
solution = Solution()
print(solution.getLucky(s, k))  # Output: 36

s = "leetcode"
k = 2
print(solution.getLucky(s, k))  # Output: 6

s = "zbax"
k = 2
print(solution.getLucky(s, k))  # Output: 8
