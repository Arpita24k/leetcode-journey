class Solution:
    def twoSum(self, numbers, target):
        """
        Find two indices such that the numbers add up to the target.

        Args:
        numbers (List[int]): Sorted 1-indexed array.
        target (int): Target sum.

        Returns:
        List[int]: Indices of the two numbers (1-based).
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-based indices
            elif current_sum < target:
                left += 1  # Move left pointer to increase the sum
            else:
                right -= 1  # Move right pointer to decrease the sum

        return []  # This will never execute because the solution is guaranteed
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    print(solution.twoSum(numbers1, target1))  # Output: [1, 2]

    # Example 2
    numbers2 = [2, 3, 4]
    target2 = 6
    print(solution.twoSum(numbers2, target2))  # Output: [1, 3]

    # Example 3
    numbers3 = [-1, 0]
    target3 = -1
    print(solution.twoSum(numbers3, target3))  # Output: [1, 2]
