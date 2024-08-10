class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) < 2:  # If less than 2 elements, no gap can be found.
            return 0

        min_val, max_val = min(nums), max(nums)  # Find the minimum and maximum values in the array.
        n = len(nums)  # Get the number of elements in the array.
        if min_val == max_val:  # If all elements are the same, the max gap is 0.
            return 0

        bucket_size = max(1, (max_val - min_val) // (n - 1))  # Calculate bucket size.
        bucket_count = (max_val - min_val) // bucket_size + 1  # Calculate the number of buckets.

        buckets_min = [float('inf')] * bucket_count  # Initialize min values for each bucket.
        buckets_max = [-float('inf')] * bucket_count  # Initialize max values for each bucket.

        for num in nums:  # Place each number in the appropriate bucket.
            bucket_idx = (num - min_val) // bucket_size  # Determine the bucket index.
            buckets_min[bucket_idx] = min(buckets_min[bucket_idx], num)  # Update bucket min.
            buckets_max[bucket_idx] = max(buckets_max[bucket_idx], num)  # Update bucket max.

        max_gap = 0  # Initialize max gap.
        previous_max = min_val  # Start with the minimum value.

        for i in range(bucket_count):  # Iterate through each bucket.
            if buckets_min[i] == float('inf'):  # Skip empty buckets.
                continue
            max_gap = max(max_gap, buckets_min[i] - previous_max)  # Update max gap.
            previous_max = buckets_max[i]  # Update previous max to current bucket's max.

        return max_gap  # Return the maximum gap found.

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums = [3, 6, 9, 1]
    print("Input:", nums)
    result = solution.maximumGap(nums)
    print("Output:", result)  # Output should be 3
    
    # Test Case 2
    nums = [10]
    print("\nInput:", nums)
    result = solution.maximumGap(nums)
    print("Output:", result)  # Output should be 0
