class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(remaining, comb, start):
            if remaining == 0:
                # If we reach the target, add the combination to the results
                result.append(list(comb))
                return
            elif remaining < 0:
                # If we exceed the target, no need to proceed further
                return
            
            for i in range(start, len(candidates)):
                # Add the number into the combination
                comb.append(candidates[i])
                # Give the current number another chance, since it can be used unlimited times
                backtrack(remaining - candidates[i], comb, i)
                # Backtrack, remove the number from the combination
                comb.pop()
        
        result = []
        backtrack(target, [], 0)
        return result

# Example usage:
candidates1 = [2, 3, 6, 7]
target1 = 7
solution = Solution()
print(solution.combinationSum(candidates1, target1))  # Output: [[2, 2, 3], [7]]

candidates2 = [2, 3, 5]
target2 = 8
print(solution.combinationSum(candidates2, target2))  # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

candidates3 = [2]
target3 = 1
print(solution.combinationSum(candidates3, target3))  # Output: []
