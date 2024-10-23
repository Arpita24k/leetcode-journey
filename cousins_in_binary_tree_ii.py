# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValuesInTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        from collections import defaultdict, deque
        
        # This will hold the values at each depth
        level_values = defaultdict(list)
        # This will hold the parent information
        parent_map = {}

        # Perform a BFS to fill level_values and parent_map
        queue = deque([(root, None, 0)])  # (node, parent, depth)
        while queue:
            node, parent, depth = queue.popleft()
            level_values[depth].append(node)
            parent_map[node] = parent

            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))

        # Calculate the cousin sums and update the tree
        for depth in level_values:
            total_sum = sum(node.val for node in level_values[depth])
            
            for node in level_values[depth]:
                # Calculate the cousin's sum
                new_val = total_sum - node.val
                # Update the node value
                node.val = new_val

        return root

# Example usage
def print_tree(node: TreeNode):
    """Helper function to print the tree in level order."""
    if not node:
        return "null"
    from collections import deque
    queue = deque([node])
    result = []
    while queue:
        current = queue.popleft()
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append("null")
    return result

# Creating a binary tree for testing
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(10)
root.right.right = TreeNode(7)

# Instantiate the solution and replace values
solution = Solution()
new_root = solution.replaceValuesInTree(root)

# Print the modified tree in level order
print(print_tree(new_root))  # Expected Output: [0, 0, 0, 7, 7, null, 11]
