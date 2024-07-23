from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        if endWord not in wordList:
            return 0
        
        # All words are of the same length
        L = len(beginWord)
        
        # Dictionary to hold all combinations of words that can be formed by changing one letter at a time
        all_combo_dict = defaultdict(list)
        
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word
                intermediate_word = word[:i] + "*" + word[i+1:]
                all_combo_dict[intermediate_word].append(word)
        
        # Queue for BFS
        queue = deque([(beginWord, 1)])  # (current word, level)
        # Visited dictionary to avoid processing the same word multiple times
        visited = {beginWord: True}
        
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                
                # Next states are all the words which share the same intermediate state
                for word in all_combo_dict[intermediate_word]:
                    # If we find the end word, we return the answer
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS queue
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                # Clear the intermediate states after processing to save memory
                all_combo_dict[intermediate_word] = []
        
        return 0

# Examples
solution = Solution()
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Output: 5
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))  # Output: 0
