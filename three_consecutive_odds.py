from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            # Check if arr[i], arr[i+1], and arr[i+2] are all odd
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
        return False

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    arr1 = [2, 6, 4, 1]
    arr2 = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    
    print(solution.threeConsecutiveOdds(arr1))  # Output: false
    print(solution.threeConsecutiveOdds(arr2))  # Output: true
