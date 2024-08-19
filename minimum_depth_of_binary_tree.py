from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])  # Queue stores tuples of (node, depth)
        
        while queue:
            node, depth = queue.popleft()
            
            # Check if this is a leaf node
            if not node.left and not node.right:
                return depth
            
            # Add left and right children to the queue if they exist
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return 0

# Example usage:
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print(solution.minDepth(root1))  # Output: 2

    # Test Case 2
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(5)
    root2.right.right.right.right = TreeNode(6)
    print(solution.minDepth(root2))  # Output: 5
