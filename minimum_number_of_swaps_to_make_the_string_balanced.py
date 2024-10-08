class Solution:
    def minSwaps(self, s: str) -> int:
        # Initialize variables to track imbalance and swaps needed
        imbalance = 0
        swaps = 0

        # Loop through each character in the string
        for char in s:
            # If we encounter an opening bracket, reduce the imbalance
            if char == '[':
                imbalance -= 1
            else:
                # If we encounter a closing bracket, increase the imbalance
                imbalance += 1

            # If imbalance becomes positive, it means we have more closing brackets than opening ones
            if imbalance > 0:
                # We need a swap to balance one closing bracket, so we increment swaps and reduce imbalance by 2
                swaps += 1
                imbalance -= 2

        return swaps

# Example usage (as it would be in LeetCode):
# You don't need to include the following in LeetCode's submission, it's just for testing locally.
if __name__ == "__main__":
    solution = Solution()
    print(solution.minSwaps("][]["))  # Output: 1
    print(solution.minSwaps("]]][[["))  # Output: 2
    print(solution.minSwaps("[]"))  # Output: 0
