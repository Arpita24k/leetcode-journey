class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()  # Sort the skill array
        
        total_skill = skill[0] + skill[-1]  # The expected total skill of each team
        chemistry_sum = 0
        n = len(skill)
        
        # Iterate over the first half of the sorted array and pair with the corresponding element from the second half
        for i in range(n // 2):
            if skill[i] + skill[n - i - 1] != total_skill:
                return -1  # If the total skill doesn't match, return -1
            
            # Calculate the chemistry and add it to the total sum
            chemistry_sum += skill[i] * skill[n - i - 1]
        
        return chemistry_sum

# Example usage:
solution = Solution()

# Testcase 1
skill1 = [3, 2, 5, 1, 3, 4]
print(f"Output: {solution.dividePlayers(skill1)}")  # Expected Output: 22

# Testcase 2
skill2 = [3, 4]
print(f"Output: {solution.dividePlayers(skill2)}")  # Expected Output: 12

# Testcase 3
skill3 = [1, 1, 2, 3]
print(f"Output: {solution.dividePlayers(skill3)}")  # Expected Output: -1
