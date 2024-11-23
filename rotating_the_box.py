class Solution:
    def rotateTheBox(self, box):
        """
        Rotate the box 90 degrees clockwise and apply gravity to stones ('#').
        
        Args:
        box (List[List[str]]): m x n matrix representing the side-view of the box.
        
        Returns:
        List[List[str]]: n x m matrix representing the box after rotation.
        """
        m, n = len(box), len(box[0])  # Dimensions of the box

        # Apply gravity to each row
        for row in box:
            empty = n - 1  # Position to place the next stone
            for col in range(n - 1, -1, -1):  # Traverse from right to left
                if row[col] == '*':  # Obstacle resets the empty position
                    empty = col - 1
                elif row[col] == '#':  # Stone falls to the empty position
                    row[col], row[empty] = '.', '#'
                    empty -= 1  # Update the empty position

        # Rotate the box 90 degrees clockwise
        rotated_box = [[box[row][col] for row in range(m - 1, -1, -1)] for col in range(n)]

        return rotated_box


# Example Usage
if __name__ == "__main__":
    # Input examples
    box1 = [["#", ".", "#"]]
    box2 = [["#", ".", "*", "."],
            ["#", "#", "*", "."]]
    box3 = [["#", "#", "*", ".", "*", "."],
            ["#", "#", "#", "*", ".", "."],
            ["#", "#", "#", ".", "#", "."]]

    # Create a Solution instance
    solution = Solution()

    # Call the function and print the results
    print("Rotated Box 1:")
    print(solution.rotateTheBox(box1))  # Output: [["."], ["#"], ["#"]]

    print("\nRotated Box 2:")
    print(solution.rotateTheBox(box2))  # Output: [["#", "."], ["#", "#"], ["*", "*"], [".", "."]]

    print("\nRotated Box 3:")
    print(solution.rotateTheBox(box3))  # Output: [[".", "#", "#"], [".", "#", "#"], ["#", "#", "*"], ["#", "*", "."], ["#", ".", "*"], ["#", ".", "."]]
