from collections import Counter
import functools

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
        @functools.lru_cache(None)
        def dfs(board, hand):
            if not board:
                return 0
            if not hand:
                return float('inf')
            
            min_steps = float('inf')
            hand_count = Counter(hand)
            
            # Try to insert a ball from hand into each possible position in the board
            for i in range(len(board) + 1):
                for ball in hand_count:
                    if hand_count[ball] > 0:
                        new_board = board[:i] + ball + board[i:]
                        new_board = remove_consecutive(new_board)
                        hand_count[ball] -= 1
                        new_hand = ''.join(sorted(hand.replace(ball, '', 1)))
                        steps = 1 + dfs(new_board, new_hand)
                        min_steps = min(min_steps, steps)
                        hand_count[ball] += 1
            
            return min_steps
        
        def remove_consecutive(board):
            i = 0
            while i < len(board):
                j = i
                while j < len(board) and board[j] == board[i]:
                    j += 1
                if j - i >= 3:
                    return remove_consecutive(board[:i] + board[j:])
                i = j
            return board
        
        result = dfs(board, ''.join(sorted(hand)))
        return result if result != float('inf') else -1

# Test cases
solution = Solution()
print(solution.findMinStep("WRRBBW", "RB"))      # Output: -1
print(solution.findMinStep("WWRRBBWW", "WRBRW")) # Output: 2
print(solution.findMinStep("G", "GGGGG"))        # Output: 2
print(solution.findMinStep("RRWWRRBBRR", "WB"))  # Output: 2
