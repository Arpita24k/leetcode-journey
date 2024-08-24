class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)
        
        # The first half of the original number
        prefix = int(n[:(length + 1) // 2])
        
        # Create potential palindrome candidates
        candidates = set()
        
        # Case 1: Mirror the prefix
        candidates.add(self.makePalindrome(prefix, length % 2 == 0))
        
        # Case 2: Mirror the prefix - 1
        candidates.add(self.makePalindrome(prefix - 1, length % 2 == 0))
        
        # Case 3: Mirror the prefix + 1
        candidates.add(self.makePalindrome(prefix + 1, length % 2 == 0))
        
        # Case 4: Special case of '999...999' or '100...001'
        candidates.add("9" * (length - 1))  # Largest palindrome smaller than n
        candidates.add("1" + "0" * (length - 1) + "1")  # Smallest palindrome larger than n
        
        # Remove the original number itself from candidates
        candidates.discard(n)
        
        # Find the closest palindrome by comparing differences
        closest_palindrome = min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
        
        return closest_palindrome
    
    def makePalindrome(self, half: int, is_even: bool) -> str:
        half_str = str(half)
        if is_even:
            return half_str + half_str[::-1]
        else:
            return half_str + half_str[:-1][::-1]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    n1 = "123"
    print(solution.nearestPalindromic(n1))  # Output: "121"
    
    # Test Case 2
    n2 = "1"
    print(solution.nearestPalindromic(n2))  # Output: "0"
