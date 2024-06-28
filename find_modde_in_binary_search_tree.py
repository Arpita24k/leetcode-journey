# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        # Helper variables to store state during traversal
        self.current_val = None
        self.current_count = 0
        self.max_count = 0
        self.modes = []
        
        def in_order(node):
            if not node:
                return
            
            # Traverse the left subtree
            in_order(node.left)
            
            # Process the current node
            if self.current_val != node.val:
                self.current_val = node.val
                self.current_count = 0
            self.current_count += 1
            
            # Check if we need to update the modes
            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.modes = [self.current_val]
            elif self.current_count == self.max_count:
                self.modes.append(self.current_val)
                
            # Traverse the right subtree
            in_order(node.right)
        
        # Start the in-order traversal
        in_order(root)
        return self.modes

# Example usage
sol = Solution()

# Building the tree: [1, null, 2, 2]
root1 = TreeNode(1, right=TreeNode(2, left=TreeNode(2)))
print(sol.findMode(root1))  # Output: [2]

# Building the tree: [0]
root2 = TreeNode(0)
print(sol.findMode(root2))  # Output: [0]
