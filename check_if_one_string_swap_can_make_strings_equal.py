from typing import List

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If strings are already equal, return True
        if s1 == s2:
            return True
        
        # Find all mismatched positions
        diff = [(s1[i], s2[i]) for i in range(len(s1)) if s1[i] != s2[i]]
        
        # There must be exactly two mismatches that can be swapped to make the strings equal
        return len(diff) == 2 and diff[0] == diff[1][::-1]

# -------------------------- Testing Code --------------------------

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("bank", "kanb", True),  # Example 1: One valid swap
        ("attack", "defend", False),  # Example 2: More than 2 mismatches
        ("kelb", "kelb", True),  # Example 3: Already equal
        ("abcd", "abdc", True),  # Swap 'c' and 'd' makes them equal
        ("abcd", "abcd", True),  # Already equal
        ("abcd", "abcf", False)  # More than 2 differences
    ]
    
    for i, (s1, s2, expected) in enumerate(test_cases, 1):
        result = solution.areAlmostEqual(s1, s2)
        print(f"Test {i}: {'PASS' if result == expected else 'FAIL'}")
