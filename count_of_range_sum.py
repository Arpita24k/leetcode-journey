#Count of Range Sum

class Solution:
    def countRangeSum(self, nums: [int], lower: int, upper: int) -> int:
        # Calculate prefix sums
        prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]

        # Function to perform modified merge sort and count the range sums
        def countWhileMergeSort(left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = countWhileMergeSort(left, mid) + countWhileMergeSort(mid + 1, right)
            j = k = t = mid + 1
            cache = []
            for i in range(left, mid + 1):
                while k <= right and prefix_sums[k] - prefix_sums[i] < lower:
                    k += 1
                while j <= right and prefix_sums[j] - prefix_sums[i] <= upper:
                    j += 1
                while t <= right and prefix_sums[t] < prefix_sums[i]:
                    cache.append(prefix_sums[t])
                    t += 1
                cache.append(prefix_sums[i])
                count += j - k
            while t <= right:
                cache.append(prefix_sums[t])
                t += 1
            prefix_sums[left:left + len(cache)] = cache
            return count

        return countWhileMergeSort(0, len(prefix_sums) - 1)

# Example usage
solution = Solution()
nums1 = [-2, 5, -1]
lower1 = -2
upper1 = 2
nums2 = [0]
lower2 = 0
upper2 = 0

print(solution.countRangeSum(nums1, lower1, upper1))  # Output: 3
print(solution.countRangeSum(nums2, lower2, upper2))  # Output: 1
