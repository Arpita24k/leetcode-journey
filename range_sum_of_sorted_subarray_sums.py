class Solution:
    def rangeSum(self, nums, n, left, right):
        MOD = 10**9 + 7  # Define the modulus to prevent overflow

        # Step 1: Generate all subarray sums
        subarray_sums = []  # Initialize an empty list to store subarray sums
        for i in range(n):  # Iterate over the starting points of subarrays
            current_sum = 0  # Initialize the current sum to 0
            for j in range(i, n):  # Iterate over the ending points of subarrays
                current_sum += nums[j]  # Add the current element to the current sum
                subarray_sums.append(current_sum)  # Append the current sum to the list

        # Step 2: Sort the list of subarray sums
        subarray_sums.sort()  # Sort the subarray sums in non-decreasing order

        # Step 3: Calculate the sum from index `left` to `right` (1-based index)
        result = 0  # Initialize the result to 0
        for k in range(left - 1, right):  # Iterate from left-1 to right-1
            result += subarray_sums[k]  # Add the subarray sum to the result
            result %= MOD  # Take the result modulo 10^9 + 7

        return result  # Return the final result

# Example usage
solution = Solution()
nums1 = [1, 2, 3, 4]
n1 = 4
left1 = 1
right1 = 5
print(solution.rangeSum(nums1, n1, left1, right1))  # Output: 13

nums2 = [1, 2, 3, 4]
n2 = 4
left2 = 3
right2 = 4
print(solution.rangeSum(nums2, n2, left2, right2))  # Output: 6

nums3 = [1, 2, 3, 4]
n3 = 4
left3 = 1
right3 = 10
print(solution.rangeSum(nums3, n3, left3, right3))  # Output: 50
