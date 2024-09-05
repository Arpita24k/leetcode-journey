# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        # Base case: if either list is empty, return None (no tree)
        if not inorder or not postorder:
            return None
        
        # The root is the last element in the postorder list
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # Find the index of the root in the inorder list
        inorder_index = inorder.index(root_val)
        
        # Recursively build the right subtree first (because we pop from the end of postorder)
        root.right = self.buildTree(inorder[inorder_index + 1:], postorder)
        
        # Recursively build the left subtree
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        
        return root

# Example usage:
solution = Solution()

# Example 1:
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
root = solution.buildTree(inorder, postorder)

# Function to print the tree in level-order to verify the structure
from collections import deque

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)
        result.append(level)
    
    # Flatten the list and remove trailing None values
    flat_result = []
    for level in result:
        flat_result.extend(level)
    while flat_result and flat_result[-1] is None:
        flat_result.pop()
    
    return flat_result

# Print the constructed tree to verify
print(levelOrder(root))  # Output: [3, 9, 20, None, None, 15, 7]

# Example 2:
inorder = [-1]
postorder = [-1]
root = solution.buildTree(inorder, postorder)
print(levelOrder(root))  # Output: [-1]
