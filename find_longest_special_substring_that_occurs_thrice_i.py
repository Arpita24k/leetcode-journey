class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        
        # Check if a substring is special
        def is_special(substr):
            return all(char == substr[0] for char in substr)
        
        # Iterate over all possible lengths, starting from the largest
        for length in range(n, 0, -1):
            count = {}
            
            # Count all substrings of the current length
            for i in range(n - length + 1):
                substr = s[i:i + length]
                
                # Only consider special substrings
                if is_special(substr):
                    count[substr] = count.get(substr, 0) + 1
            
            # Check if any special substring occurs at least three times
            for substr, freq in count.items():
                if freq >= 3:
                    return length
        
        # No valid substring found
        return -1

# Example usage
solution = Solution()

# Test cases
print(solution.maximumLength("aaaa"))     # Output: 2
print(solution.maximumLength("abcdef"))   # Output: -1
print(solution.maximumLength("abcaba"))   # Output: 1
