class Solution:
    def partition(self, s: str):
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, path):
            # If we have reached the end of the string, add the current partition to the result
            if start == len(s):
                result.append(path[:])
                return
            
            for end in range(start + 1, len(s) + 1):
                # If the current substring is a palindrome
                if is_palindrome(s[start:end]):
                    # Recur with the next part of the string
                    backtrack(end, path + [s[start:end]])
        
        result = []
        backtrack(0, [])
        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s1 = "aab"
    print(solution.partition(s1))  # Output: [["a","a","b"],["aa","b"]]
    
    # Test Case 2
    s2 = "a"
    print(solution.partition(s2))  # Output: [["a"]]
