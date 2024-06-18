from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convertListToBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # Always choose the middle element to maintain balance
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # Recursively build the left and right subtrees
            node.left = convertListToBST(left, mid - 1)
            node.right = convertListToBST(mid + 1, right)
            return node
        
        return convertListToBST(0, len(nums) - 1)

def levelOrder(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = [(root, 0)]
    current_level = 0
    current_level_nodes = []
    
    while queue:
        node, level = queue.pop(0)
        if level == current_level:
            current_level_nodes.append(node.val if node else None)
        else:
            result.extend(current_level_nodes)
            current_level_nodes = [node.val if node else None]
            current_level = level
        
        if node:
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
    
    result.extend(current_level_nodes)
    
    # Trim the trailing None values for correct representation
    while result and result[-1] is None:
        result.pop()
    
    return result

# Example usage
solution = Solution()

nums1 = [-10, -3, 0, 5, 9]
nums2 = [1, 3]

root1 = solution.sortedArrayToBST(nums1)
root2 = solution.sortedArrayToBST(nums2)

print("Tree from nums1:")
print(levelOrder(root1))  # Output should be [0, -3, 9, -10, None, 5]

print("Tree from nums2:")
print(levelOrder(root2))  # Output should be [1, None, 3]
