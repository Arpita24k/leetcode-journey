from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ ent appears twice except for one.
        It finds and returns the element that appears only once.
        
        :param nums: List[int] - List of integers
        :return: int - The single number that appears only once
        """
        # Initialize the result variable to 0
        result = 0
        
        # Iterate through each number in the list
        for n in nums:
            # Use XOR operation to cancel out pairs of identical numbers
            # and leave the unique number
            result ^= n
        
        # Print the result, which is the single number that appears only once
        print(f"The single number in the list is: {result}")
        
        # Return the result
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [4, 1, 2, 1, 2]
    solution.singleNumber(nums)
