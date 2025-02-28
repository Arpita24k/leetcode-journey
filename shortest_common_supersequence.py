class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        Returns the shortest common supersequence (SCS) of str1 and str2.

        Args:
        str1 (str): First input string.
        str2 (str): Second input string.

        Returns:
        str: The shortest string that has both str1 and str2 as subsequences.
        """
        m, n = len(str1), len(str2)
        
        # Step 1: Compute LCS using DP
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Step 2: Build the SCS using the LCS table
        i, j = m, n
        scs = []
        
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  # LCS character
                scs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:  # Take from str1
                scs.append(str1[i - 1])
                i -= 1
            else:  # Take from str2
                scs.append(str2[j - 1])
                j -= 1

        # Add remaining characters from str1 or str2
        while i > 0:
            scs.append(str1[i - 1])
            i -= 1
        while j > 0:
            scs.append(str2[j - 1])
            j -= 1
        
        return "".join(reversed(scs))
