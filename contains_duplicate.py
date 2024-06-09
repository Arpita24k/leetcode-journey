from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a set to track the elements we have seen
        seen = set()
        
        # Iterate through each number in the list
        for num in nums:
            # If the number is already in the set, return True
            if num in seen:
                print("Contains duplicates:", True)
                return True
            # Otherwise, add the number to the set
            seen.add(num)
        
        # If we finish the loop without finding duplicates, return False
        print("Contains duplicates:", False)
        return False

# Example usage
solution = Solution()
nums = [1, 2, 3, 1]
solution.containsDuplicate(nums)
