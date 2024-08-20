def stoneGameII(piles):
    n = len(piles)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    sum_piles = [0] * (n + 1)
    
    # Calculate the cumulative sum from the end
    for i in range(n - 1, -1, -1):
        sum_piles[i] = sum_piles[i + 1] + piles[i]
    
    # Bottom-up DP
    for i in range(n - 1, -1, -1):
        for M in range(1, n + 1):
            max_stones = 0
            for X in range(1, 2 * M + 1):
                if i + X <= n:
                    max_stones = max(max_stones, sum_piles[i] - dp[i + X][max(M, X)])
            dp[i][M] = max_stones
    
    return dp[0][1]

# Example usage:
if __name__ == "__main__":
    # Test Case 1
    piles1 = [2, 7, 9, 4, 4]
    print(stoneGameII(piles1))  # Output: 10
    
    # Test Case 2
    piles2 = [1, 2, 3, 4, 5, 100]
    print(stoneGameII(piles2))  # Output: 104
