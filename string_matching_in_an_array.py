class Solution:
    def stringMatching(self, words):
        """
        Given an array of words, return all strings in words that are substrings of another word.
        """
        result = []
        
        # Check every word against every other word
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:  # Check if word[i] is a substring of word[j]
                    result.append(words[i])
                    break  # Avoid duplicates by breaking once found
                    
        return result
