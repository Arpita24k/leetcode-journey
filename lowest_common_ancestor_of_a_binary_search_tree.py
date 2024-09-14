# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Traverse the tree
        current = root
        
        while current:
            # If both p and q are smaller than current, go left
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If both p and q are greater than current, go right
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                # We have found the split point, i.e., the LCA
                return current

# Example usage:
# Create the tree: [6,2,8,0,4,7,9,null,null,3,5]
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

solution = Solution()

# Example 1:
p = root.left  # Node with value 2
q = root.right  # Node with value 8
print(solution.lowestCommonAncestor(root, p, q).val)  # Output: 6

# Example 2:
p = root.left  # Node with value 2
q = root.left.right  # Node with value 4
print(solution.lowestCommonAncestor(root, p, q).val)  # Output: 2

# Example 3:
root2 = TreeNode(2)
root2.left = TreeNode(1)
p = root2  # Node with value 2
q = root2.left  # Node with value 1
print(solution.lowestCommonAncestor(root2, p, q).val)  # Output: 2
