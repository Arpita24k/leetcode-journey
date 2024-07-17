class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []
        
        def dfs(node, is_root):
            if not node:
                return None
            root_deleted = node.val in to_delete_set
            if is_root and not root_deleted:
                forest.append(node)
            node.left = dfs(node.left, root_deleted)
            node.right = dfs(node.right, root_deleted)
            return None if root_deleted else node
        
        dfs(root, True)
        return forest

# Example usage:
# Construct the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

solution = Solution()
result = solution.delNodes(root, [3, 5])
# To display the resulting forest:
def serialize(root):
    """Encodes a tree to a single string."""
    def preorder(node):
        if not node:
            return []
        return [node.val] + preorder(node.left) + preorder(node.right)
    return preorder(root)

# Serialize and print each tree in the resulting forest
for tree in result:
    print(serialize(tree))
# Output: [[1, 2, 4], [6], [7]]
