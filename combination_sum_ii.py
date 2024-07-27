class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        candidates.sort()  # Sort the candidates to handle duplicates easily
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Include candidates[i] in the combination and recurse
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return result

# Examples
solution = Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5], 8))  # Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
print(solution.combinationSum2([2,5,2,1,2], 5))  # Output: [[1,2,2],[5]]
