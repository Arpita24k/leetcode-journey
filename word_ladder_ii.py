from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # Dictionary to hold the parents of each word
        parents = defaultdict(list)
        # Level dictionary to track the BFS level of each word
        level = {beginWord: 0}
        
        # Initialize BFS
        queue = deque([beginWord])
        found = False
        word_len = len(beginWord)
        
        while queue and not found:
            next_level = defaultdict(list)
            for _ in range(len(queue)):
                word = queue.popleft()
                current_level = level[word]
                
                for i in range(word_len):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            if new_word not in level:
                                level[new_word] = current_level + 1
                                queue.append(new_word)
                                parents[new_word].append(word)
                            elif level[new_word] == current_level + 1:
                                parents[new_word].append(word)
                            if new_word == endWord:
                                found = True
            
            wordSet -= set(queue)
        
        def backtrack(word):
            if word == beginWord:
                return [[beginWord]]
            return [[word] + path for parent in parents[word] for path in backtrack(parent)]
        
        # Generate paths and reverse them to get correct order
        paths = backtrack(endWord)
        return [path[::-1] for path in paths]

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(solution.findLadders(beginWord, endWord, wordList))
    # Expected Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    
    # Test Case 2
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    print(solution.findLadders(beginWord, endWord, wordList))
    # Expected Output: []
