class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If the lengths of the strings are different, they cannot be isomorphic
        if len(s) != len(t):
            return False

        # Create two dictionaries to store character mappings
        s_to_t_mapping = {}
        t_to_s_mapping = {}

        # Iterate through characters of both strings simultaneously
        for char_s, char_t in zip(s, t):
            # Check mapping from s to t
            if char_s in s_to_t_mapping:
                if s_to_t_mapping[char_s] != char_t:
                    return False
            else:
                s_to_t_mapping[char_s] = char_t

            # Check mapping from t to s
            if char_t in t_to_s_mapping:
                if t_to_s_mapping[char_t] != char_s:
                    return False
            else:
                t_to_s_mapping[char_t] = char_s

        # If all character mappings are consistent, return True
        return True

# Example usage:
solution = Solution()

print(solution.isIsomorphic("egg", "add"))      # Output: True
print(solution.isIsomorphic("foo", "bar"))      # Output: False
print(solution.isIsomorphic("paper", "title"))  # Output: True
print(solution.isIsomorphic("ab", "aa"))        # Output: False
