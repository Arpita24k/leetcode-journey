class Solution:
    def majorityElement(self, nums):
        # Step 1: Identify potential candidates
        candidate1, candidate2, count1, count2 = None, None, 0, 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify the candidates
        result = []
        n = len(nums)
        if nums.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate2 is not None and nums.count(candidate2) > n // 3:
            result.append(candidate2)

        return result

# Example usage
solution = Solution()

# Test case 1
nums1 = [3, 2, 3]
print("Output for nums1:", solution.majorityElement(nums1))  # Expected: [3]

# Test case 2
nums2 = [1]
print("Output for nums2:", solution.majorityElement(nums2))  # Expected: [1]

# Test case 3
nums3 = [1, 2]
print("Output for nums3:", solution.majorityElement(nums3))  # Expected: [1, 2]
