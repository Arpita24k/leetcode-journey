class Solution:
    def applyOperations(self, nums):
        """
        Applies operations to modify the array as described and returns the result.

        Args:
        nums (List[int]): Input array of non-negative integers.

        Returns:
        List[int]: The resulting array after operations and shifting zeros.
        """
        n = len(nums)

        # Step 1: Apply in-place operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0

        # Step 2: Shift zeros to the end
        result = [num for num in nums if num != 0]
        result.extend([0] * (n - len(result)))
        
        return result
