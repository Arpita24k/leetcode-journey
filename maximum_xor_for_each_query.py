class Solution:
    def getMaximumXor(self, nums, maximumBit):
        # Step 1: Calculate initial XOR of all elements
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        
        # Step 2: Calculate the maximum number (bitmask) we can use
        bitmask = (1 << maximumBit) - 1
        
        # Step 3: Generate answers by modifying xor_sum as we "remove" elements from the end
        answer = []
        for num in reversed(nums):
            answer.append(xor_sum ^ bitmask)  # Maximum k value for the current xor_sum
            xor_sum ^= num  # Remove last element by XORing it out
        
        return answer

# Example usage:
solution = Solution()

# Test case 1
nums1 = [0, 1, 1, 3]
maximumBit1 = 2
print("Output for nums1:", solution.getMaximumXor(nums1, maximumBit1))  # Expected: [0, 3, 2, 3]

# Test case 2
nums2 = [2, 3, 4, 7]
maximumBit2 = 3
print("Output for nums2:", solution.getMaximumXor(nums2, maximumBit2))  # Expected: [5, 2, 6, 5]

# Test case 3
nums3 = [0, 1, 2, 2, 5, 7]
maximumBit3 = 3
print("Output for nums3:", solution.getMaximumXor(nums3, maximumBit3))  # Expected: [4, 3, 6, 4, 6, 7]
