from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        
        # Sort the envelopes: first by width ascending, then by height descending for ties
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Extract the heights from the sorted envelopes
        heights = [h for _, h in envelopes]
        
        # Find the longest increasing subsequence in heights using a dynamic array and binary search
        lis = []
        
        for height in heights:
            pos = bisect_left(lis, height)
            if pos == len(lis):
                lis.append(height)
            else:
                lis[pos] = height
        
        # The length of lis is the maximum number of envelopes that can be Russian dolled
        return len(lis)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    envelopes1 = [[5,4],[6,4],[6,7],[2,3]]
    print(solution.maxEnvelopes(envelopes1))  # Output: 3
    
    # Test Case 2
    envelopes2 = [[1,1],[1,1],[1,1]]
    print(solution.maxEnvelopes(envelopes2))  # Output: 1
