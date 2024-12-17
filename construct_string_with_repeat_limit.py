import heapq
from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Step 1: Count the frequency of each character
        char_count = Counter(s)
        
        # Step 2: Use a max-heap to store characters by their ASCII order (negative for max-heap)
        max_heap = []
        for char, freq in char_count.items():
            heapq.heappush(max_heap, (-ord(char), char, freq))  # (negative ASCII, char, frequency)
        
        result = []
        
        while max_heap:
            # Pop the largest character
            _, char, freq = heapq.heappop(max_heap)
            
            # Add the character up to repeatLimit times
            use_count = min(freq, repeatLimit)
            result.append(char * use_count)
            
            remaining = freq - use_count
            
            # If the current character cannot be used fully and we have remaining heap elements
            if remaining > 0:
                if not max_heap:
                    # If there are no other characters to break the repetition, stop
                    break
                
                # Use the next largest character to break the repetition
                _, next_char, next_freq = heapq.heappop(max_heap)
                result.append(next_char)  # Append one instance of the next character
                
                # Reinsert the next character into the heap with updated frequency
                if next_freq > 1:
                    heapq.heappush(max_heap, (-ord(next_char), next_char, next_freq - 1))
                
                # Reinsert the current character with the remaining count
                heapq.heappush(max_heap, (-ord(char), char, remaining))
        
        return ''.join(result)

# Example usage
solution = Solution()

# Example 1
s = "cczazcc"
repeatLimit = 3
print(solution.repeatLimitedString(s, repeatLimit))  # Output: "zzcccac"

# Example 2
s = "aababab"
repeatLimit = 2
print(solution.repeatLimitedString(s, repeatLimit))  # Output: "bbabaa"
