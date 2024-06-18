from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            # If both nodes are None, they are symmetric
            if not t1 and not t2:
                return True
            # If only one of the nodes is None, they are not symmetric
            if not t1 or not t2:
                return False
            # Check if the current nodes' values are equal and the left subtree of t1 is a mirror of the right subtree of t2 and vice versa
            return (t1.val == t2.val and
                    isMirror(t1.right, t2.left) and
                    isMirror(t1.left, t2.right))
        
        # A tree is symmetric if the left and right subtrees are mirrors of each other
        return isMirror(root, root)

def createBinaryTree(arr: list, index: int = 0) -> Optional[TreeNode]:
    """
    Helper function to create a binary tree from a list representation.
    :param arr: List representation of the tree (None signifies the absence of a node)
    :param index: Current index in the list
    :return: Root of the binary tree
    """
    if index < len(arr) and arr[index] is not None:
        node = TreeNode(arr[index])
        node.left = createBinaryTree(arr, 2 * index + 1)
        node.right = createBinaryTree(arr, 2 * index + 2)
        return node
    return None

def printTree(root: Optional[TreeNode]) -> None:
    """
    Helper function to print the tree level-by-level (BFS)
    """
    if not root:
        print("Empty tree")
        return
    
    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            print(node.val, end=" ")
            queue.append(node.left)
            queue.append(node.right)
        else:
            print("None", end=" ")
    print()

# Example usage
solution = Solution()

root1 = createBinaryTree([1, 2, 2, 3, 4, 4, 3])
root2 = createBinaryTree([1, 2, 2, None, 3, None, 3])

print("Tree 1:")
printTree(root1)
print("Is Tree 1 symmetric?", solution.isSymmetric(root1))  # Output: True

print("\nTree 2:")
printTree(root2)
print("Is Tree 2 symmetric?", solution.isSymmetric(root2))  # Output: False
