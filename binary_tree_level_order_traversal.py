from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        
        return result

def createBinaryTree(arr: List[Optional[int]], index: int = 0) -> Optional[TreeNode]:
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

# Example usage
solution = Solution()

root1 = createBinaryTree([3, 9, 20, None, None, 15, 7])
root2 = createBinaryTree([1])
root3 = createBinaryTree([])

print("Level order traversal of Tree 1:")
print(solution.levelOrder(root1))  # Output: [[3],[9,20],[15,7]]

print("\nLevel order traversal of Tree 2:")
print(solution.levelOrder(root2))  # Output: [[1]]

print("\nLevel order traversal of Tree 3:")
print(solution.levelOrder(root3))  # Output: []
