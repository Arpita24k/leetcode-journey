class Solution:
    def constructDistancedSequence(self, n):
        size = 2 * n - 1  # Length of the sequence
        result = [0] * size  # Initialize array with zeros
        used = set()  # To track placed numbers
        
        def backtrack(index):
            if index == size:  # If we filled all slots
                return True
            
            if result[index] != 0:  # Skip filled positions
                return backtrack(index + 1)
            
            # Try placing numbers from n down to 1
            for num in range(n, 0, -1):
                if num in used:
                    continue  # Skip numbers already used
                
                if num == 1:  # 1 appears only once
                    result[index] = 1
                    used.add(1)
                    if backtrack(index + 1):  # Move to the next index
                        return True
                    result[index] = 0  # Undo choice
                    used.remove(1)
                
                else:  # Other numbers appear twice
                    if index + num < size and result[index] == 0 and result[index + num] == 0:
                        result[index] = num
                        result[index + num] = num
                        used.add(num)
                        
                        if backtrack(index + 1):  # Move to the next index
                            return True
                        
                        # Undo choice (backtrack)
                        result[index] = 0
                        result[index + num] = 0
                        used.remove(num)
            
            return False
        
        backtrack(0)
        return result
