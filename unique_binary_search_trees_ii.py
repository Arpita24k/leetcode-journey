# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []

        def generateTrees(start, end):
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end + 1):
                # Generate all possible left subtrees with values less than i
                left_trees = generateTrees(start, i - 1)

                # Generate all possible right subtrees with values greater than i
                right_trees = generateTrees(i + 1, end)

                # Combine all possible left and right subtrees with the current root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        return generateTrees(1, n)

# Example usage:
def print_tree(node):
    """Helper function to print the tree nodes in a structured way."""
    if not node:
        return "null"
    left = print_tree(node.left)
    right = print_tree(node.right)
    return f"[{node.val}, {left}, {right}]"

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    n = 3
    all_trees = solution.generateTrees(n)
    for tree in all_trees:
        print(print_tree(tree))  # Prints all unique BSTs with n = 3
    
    # Test Case 2
    n = 1
    all_trees = solution.generateTrees(n)
    for tree in all_trees:
        print(print_tree(tree))  # Prints all unique BSTs with n = 1
