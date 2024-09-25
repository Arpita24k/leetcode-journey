class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0  # Tracks how many words have this prefix

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
    
    def count_prefixes(self, word):
        node = self.root
        total_score = 0
        for char in word:
            if char in node.children:
                node = node.children[char]
                total_score += node.prefix_count
            else:
                break
        return total_score

class Solution:
    def sumPrefixScores(self, words):
        trie = Trie()
        
        # Insert all words into the Trie
        for word in words:
            trie.insert(word)
        
        # Calculate the score for each word
        result = []
        for word in words:
            result.append(trie.count_prefixes(word))
        
        return result

# Example usage:
solution = Solution()

# Example 1:
words = ["abc","ab","bc","b"]
print(solution.sumPrefixScores(words))  # Output: [5, 4, 3, 2]

# Example 2:
words = ["abcd"]
print(solution.sumPrefixScores(words))  # Output: [4]
