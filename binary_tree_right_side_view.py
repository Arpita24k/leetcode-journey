from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        
        right_view = []
        queue = deque([root])
        
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                # If it's the last node in the level, add it to the result
                if i == level_length - 1:
                    right_view.append(node.val)
                
                # Add the child nodes in the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right_view

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    print(solution.rightSideView(root1))  # Output: [1, 3, 4]

    # Example 2
    root2 = TreeNode(1)
    root2.right = TreeNode(3)
    print(solution.rightSideView(root2))  # Output: [1, 3]

    # Example 3
    root3 = None
    print(solution.rightSideView(root3))  # Output: []
