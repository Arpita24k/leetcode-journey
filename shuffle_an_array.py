import random

class Solution:
    def __init__(self, nums: list[int]):
        self.original = nums[:]  # Store a copy of the original array
        self.array = nums[:]     # Create a working copy that we will shuffle

    def reset(self) -> list[int]:
        # Reset the working array to the original configuration
        self.array = self.original[:]
        return self.array

    def shuffle(self) -> list[int]:
        # Perform the Fisher-Yates shuffle on the array
        for i in range(len(self.array) - 1, 0, -1):
            j = random.randint(0, i)  # Select a random index from 0 to i
            self.array[i], self.array[j] = self.array[j], self.array[i]  # Swap elements
        return self.array
# Example usage:
solution = Solution([1, 2, 3])
print(solution.shuffle())  # Shuffle the array randomly, e.g., [3, 1, 2]
print(solution.reset())    # Reset to original configuration, [1, 2, 3]
print(solution.shuffle())  # Shuffle again, e.g., [2, 3, 1]
