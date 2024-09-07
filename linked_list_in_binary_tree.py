class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # Helper function to match the linked list along the tree
        def dfs(head, node):
            if not head:
                return True  # Reached the end of the linked list successfully
            if not node:
                return False  # Reached a dead end in the tree
            if head.val != node.val:
                return False  # Values do not match
            
            # Try to match the next linked list node in either left or right child
            return dfs(head.next, node.left) or dfs(head.next, node.right)
        
        # Main function to try starting the list from every node in the tree
        if not root:
            return False
        
        # Either the current node starts the path, or we try the left or right subtrees
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

# Example usage:

# Linked list: 4 -> 2 -> 8
head = ListNode(4, ListNode(2, ListNode(8)))

# Binary Tree: 
#     1
#    / \
#   4   4
#    \   \
#     2   2
#    /   / \
#   1   6   8
#  /       / \
# 1       1   3

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root.left.right.left.left = TreeNode(1)
root.right.right = TreeNode(2)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(8)
root.right.right.right.left = TreeNode(1)
root.right.right.right.right = TreeNode(3)

sol = Solution()
print(sol.isSubPath(head, root))  # Output: True
