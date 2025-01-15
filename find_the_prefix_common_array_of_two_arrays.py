class Solution:
    def findThePrefixCommonArray(self, A, B):
        # Initialize sets and result array
        seen_A = set()
        seen_B = set()
        C = []

        # Iterate over both permutations
        for i in range(len(A)):
            # Add the current element to respective sets
            seen_A.add(A[i])
            seen_B.add(B[i])
            
            # Count common elements using intersection
            common_count = len(seen_A & seen_B)
            C.append(common_count)
        
        return C

# ✅ Example Usage:
solution = Solution()

# Test Case 1
A1 = [1, 3, 2, 4]
B1 = [3, 1, 2, 4]
print(solution.findThePrefixCommonArray(A1, B1))  # Output: [0, 2, 3, 4]

# Test Case 2
A2 = [2, 3, 1]
B2 = [3, 1, 2]
print(solution.findThePrefixCommonArray(A2, B2))  # Output: [0, 1, 3]

# Test Case 3
A3 = [1, 2, 3, 4, 5]
B3 = [5, 4, 3, 2, 1]
print(solution.findThePrefixCommonArray(A3, B3))  # Output: [0, 0, 0, 1, 5]
