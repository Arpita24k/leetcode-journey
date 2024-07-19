from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t that need to be present in the window.
        required = len(dict_t)

        # Left and Right pointer
        l, r = 0, 0

        # Formed is used to keep track of how many unique characters in t
        # are present in the current window in their desired frequency.
        # e.g. if t is "AABC" then the window must have two 'A's, one 'B' and one 'C'.
        # Thus formed would be incremented only when the count of a character in the
        # current window matches its count in t.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = defaultdict(int)

        # (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] += 1

            # If the frequency of the current character added equals to the
            # desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer
                # a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

# Example usage:
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(solution.minWindow("a", "a"))  # Output: "a"
print(solution.minWindow("a", "aa"))  # Output: ""
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t that need to be present in the window.
        required = len(dict_t)

        # Left and Right pointer
        l, r = 0, 0

        # Formed is used to keep track of how many unique characters in t
        # are present in the current window in their desired frequency.
        # e.g. if t is "AABC" then the window must have two 'A's, one 'B' and one 'C'.
        # Thus formed would be incremented only when the count of a character in the
        # current window matches its count in t.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = defaultdict(int)

        # (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] += 1

            # If the frequency of the current character added equals to the
            # desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer
                # a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1    

            # Keep expanding the window once we are done contracting.
            r += 1    

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

# Example usage:
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(solution.minWindow("a", "a"))  # Output: "a"
print(solution.minWindow("a", "aa"))  # Output: ""
