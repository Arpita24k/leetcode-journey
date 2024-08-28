from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        
        results = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add the current level's nodes to results in the correct order
            if left_to_right:
                results.append(level_nodes)
            else:
                results.append(level_nodes[::-1])
            
            # Toggle the direction
            left_to_right = not left_to_right
        
        return results

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(solution.zigzagLevelOrder(root1))  # Output: [[3], [20, 9], [15, 7]]
    
    # Test Case 2
    root2 = TreeNode(1)
    print(solution.zigzagLevelOrder(root2))  # Output: [[1]]
    
    # Test Case 3
    root3 = None
    print(solution.zigzagLevelOrder(root3))  # Output: []
