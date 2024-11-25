from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        """
        Solves the sliding puzzle using BFS to find the least number of moves.

        Args:
        board (List[List[int]]): Initial board configuration.

        Returns:
        int: Minimum number of moves to solve the board, or -1 if impossible.
        """
        # Flatten the board into a string
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"  # Solved state

        # Neighbor mapping for each position on a 2x3 board
        neighbors = {
            0: [1, 3],    # Neighbors of position 0
            1: [0, 2, 4], # Neighbors of position 1
            2: [1, 5],    # Neighbors of position 2
            3: [0, 4],    # Neighbors of position 3
            4: [1, 3, 5], # Neighbors of position 4
            5: [2, 4]     # Neighbors of position 5
        }

        # BFS initialization
        queue = deque([(start, start.index('0'), 0)])  # (state, zero_pos, moves)
        visited = set()
        visited.add(start)

        while queue:
            state, zero_pos, moves = queue.popleft()

            # Check if the current state is the target
            if state == target:
                return moves

            # Explore neighbors by swapping '0' with adjacent tiles
            for neighbor in neighbors[zero_pos]:
                new_state = list(state)
                # Swap zero with the neighbor
                new_state[zero_pos], new_state[neighbor] = new_state[neighbor], new_state[zero_pos]
                new_state_str = ''.join(new_state)

                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, neighbor, moves + 1))

        return -1  # If no solution is found
