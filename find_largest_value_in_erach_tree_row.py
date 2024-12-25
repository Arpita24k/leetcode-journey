# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root):
        """
        Find the largest value in each row of a binary tree.

        Args:
        root (TreeNode): The root of the binary tree.

        Returns:
        List[int]: An array of the largest values in each row.
        """
        if not root:
            return []

        result = []
        queue = deque([root])  # Initialize the queue with the root

        while queue:
            level_size = len(queue)  # Number of nodes in the current level
            max_value = float('-inf')  # Track the maximum value in the level
            
            for _ in range(level_size):
                node = queue.popleft()
                max_value = max(max_value, node.val)  # Update the max value
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(max_value)  # Append the max value for the current level

        return result
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)
    root1.left.right = TreeNode(3)
    root1.right.right = TreeNode(9)

    solution = Solution()
    print(solution.largestValues(root1))  # Output: [1, 3, 9]

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    print(solution.largestValues(root2))  # Output: [1, 3]

    # Example 3: Empty tree
    print(solution.largestValues(None))  # Output: []
