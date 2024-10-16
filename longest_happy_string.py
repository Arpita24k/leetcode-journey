import heapq  # Importing heapq to manage the maximum occurrences easily

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a max heap based on the frequency of 'a', 'b', 'c'
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))  # Push 'a' with its count
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))  # Push 'b' with its count
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))  # Push 'c' with its count
        
        result = []  # To store the resultant happy string

        while max_heap:
            # Pop the most frequent character
            count1, char1 = heapq.heappop(max_heap)
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                # If the last two characters are the same, choose the next character
                if not max_heap:  # If no other characters are available, break
                    break
                count2, char2 = heapq.heappop(max_heap)
                result.append(char2)  # Add the second most frequent character
                if count2 + 1:  # If there are more of this character, push it back
                    heapq.heappush(max_heap, (count2 + 1, char2))
                heapq.heappush(max_heap, (count1, char1))  # Push the original character back
            else:
                # Add the most frequent character if no three consecutive restriction
                result.append(char1)
                if count1 + 1:  # If there are more of this character, push it back
                    heapq.heappush(max_heap, (count1 + 1, char1))

        return ''.join(result)  # Join the list into a string and return

# Usage Example
solution = Solution()
print(solution.longestDiverseString(1, 1, 7))  # Output: "ccaccbcc"
print(solution.longestDiverseString(7, 1, 0))  # Output: "aabaa"