class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = 2 * (n - 1)
        effective_time = time % cycle_length
        
        if effective_time < n:
            return effective_time + 1
        else:
            return cycle_length - effective_time + 1

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.passThePillow(4, 5))  # Output: 2
    print(solution.passThePillow(3, 2))  # Output: 3
