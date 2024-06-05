def rotate(nums, k):
    """
    Rotate an array to the right by k steps.

    :param nums: List[int] - The list of numbers to rotate.
    :param k: int - The number of steps to rotate the array.
    """
    n = len(nums)
    k = k % n  # In case k is greater than the length of nums
    nums[:] = nums[-k:] + nums[:-k]

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"Original array: {arr}")
    rotate(arr, k)
    print(f"Array after rotating {k} steps: {arr}")
