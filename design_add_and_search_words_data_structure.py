class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes
        self.children = {}
        # Boolean flag to indicate the end of a word
        self.is_end = False

class WordDictionary:
    def __init__(self):
        # Initialize the root of the Trie
        self.root = TrieNode()

    # Method to add a word to the Trie
    def addWord(self, word: str) -> None:
        current = self.root
        # Traverse the Trie and add each character
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        # Mark the end of the word
        current.is_end = True

    # Helper method to search the word with support for the dot character
    def search_in_node(self, word: str, node: TrieNode) -> bool:
        for i, char in enumerate(word):
            if char == '.':
                # Dot found, try all possible children
                for child in node.children.values():
                    if self.search_in_node(word[i+1:], child):
                        return True
                return False
            else:
                # If the character is not found, return False
                if char not in node.children:
                    return False
                node = node.children[char]
        return node.is_end

    # Method to search for a word, supporting the dot character
    def search(self, word: str) -> bool:
        return self.search_in_node(word, self.root)

# Example usage:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")

# Search for words
print(wordDictionary.search("pad"))  # Output: False
print(wordDictionary.search("bad"))  # Output: True
print(wordDictionary.search(".ad"))  # Output: True
print(wordDictionary.search("b.."))  # Output: True
