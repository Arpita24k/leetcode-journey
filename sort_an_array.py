class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left

            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        def heapSort(arr):
            n = len(arr)

            # Build a max heap
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)

            # Extract elements one by one
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]  # Swap
                heapify(arr, i, 0)

        heapSort(nums)
        return nums

# Examples
solution = Solution()
print(solution.sortArray([5, 2, 3, 1]))  # Output: [1, 2, 3, 5]
print(solution.sortArray([5, 1, 1, 2, 0, 0]))  # Output: [0, 0, 1, 1, 2, 5]
