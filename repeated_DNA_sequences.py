class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []

        sequence_map = {}
        result = []

        # Traverse through the string with a window of size 10
        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            if sequence in sequence_map:
                sequence_map[sequence] += 1
            else:
                sequence_map[sequence] = 1
            
            # Add to the result if the sequence appears twice (we only add it once)
            if sequence_map[sequence] == 2:
                result.append(sequence)

        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(solution.findRepeatedDnaSequences(s1))  # Output: ["AAAAACCCCC", "CCCCCAAAAA"]

    # Test Case 2
    s2 = "AAAAAAAAAAAAA"
    print(solution.findRepeatedDnaSequences(s2))  # Output: ["AAAAAAAAAA"]
