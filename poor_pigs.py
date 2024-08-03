import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Calculate the number of tests we can conduct
        tests = minutesToTest // minutesToDie
        
        # Calculate the minimum number of pigs needed
        # We need the smallest number of pigs `p` such that (tests + 1)^p >= buckets
        pigs = math.ceil(math.log(buckets) / math.log(tests + 1))
        
        return pigs

# Example usage
solution = Solution()
print(solution.poorPigs(4, 15, 15))  # Output: 2
print(solution.poorPigs(4, 15, 30))  # Output: 2
print(solution.poorPigs(1000, 15, 60))  # Example with larger numbers
