class Solution:
    def pivotArray(self, nums, pivot):
        less_than = []
        equal_to = []
        greater_than = []

        # Three-pass approach to separate elements
        for num in nums:
            if num < pivot:
                less_than.append(num)
            elif num == pivot:
                equal_to.append(num)
            else:
                greater_than.append(num)

        # Concatenate results
        return less_than + equal_to + greater_than
