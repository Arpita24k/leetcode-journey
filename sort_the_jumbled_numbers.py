class Solution:
    def sortJumbled(self, mapping: [int], nums: [int]) -> [int]:
        def get_mapped_value(num):
            mapped_num = ""
            for digit in str(num):
                mapped_num += str(mapping[int(digit)])
            return int(mapped_num)
        
        # Use the custom key to sort the nums array
        return sorted(nums, key=get_mapped_value)

# Examples
solution = Solution()
print(solution.sortJumbled([8,9,4,0,2,1,3,5,7,6], [991, 338, 38]))  # Output: [338, 38, 991]
print(solution.sortJumbled([0,1,2,3,4,5,6,7,8,9], [789, 456, 123]))  # Output: [123, 456, 789]
