class Solution:
    def fullJustify(self, words, maxWidth):
        """
        Function to format the text such that each line has exactly maxWidth characters and is fully justified.
        
        Args:
        words: List of strings.
        maxWidth: Integer, the maximum width of each line.
        
        Returns:
        List of strings representing the justified text.
        """
        result = []
        current_line = []
        current_length = 0
        
        for word in words:
            # Check if adding the new word would exceed maxWidth
            if current_length + len(word) + len(current_line) > maxWidth:
                # Justify the current line
                for i in range(maxWidth - current_length):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                result.append(''.join(current_line))
                # Reset for the next line
                current_line, current_length = [], 0
            
            # Add the word to the current line
            current_line.append(word)
            current_length += len(word)
        
        # Handle the last line (left-justified)
        result.append(' '.join(current_line).ljust(maxWidth))
        
        return result

# Example usage
solution = Solution()
print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

print(solution.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]

print(solution.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
