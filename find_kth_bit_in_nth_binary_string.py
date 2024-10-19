class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Recursive function to find the k-th bit
        def findKth(n, k):
            # Base case: If n == 1, the string S1 is "0"
            if n == 1:
                return '0'
            
            length = (1 << n) - 1  # Length of Sn, which is 2^n - 1
            mid = (length // 2) + 1  # The middle index of Sn

            if k == mid:
                return '1'  # The middle bit is always '1'
            elif k < mid:
                return findKth(n - 1, k)  # In the first half, same as Sn-1
            else:
                # In the second half, find the mirrored position and invert it
                mirrored_pos = length - k + 1
                return '1' if findKth(n - 1, mirrored_pos) == '0' else '0'
        
        return findKth(n, k)

# Usage example:
solution = Solution()
print(solution.findKthBit(3, 1))  # Output: "0"
print(solution.findKthBit(4, 11))  # Output: "1"
