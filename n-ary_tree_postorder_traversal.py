# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: Node):
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            # Extend the stack with the children (children are processed right-to-left)
            stack.extend(node.children)
        
        # Reverse the result to get the postorder sequence
        return result[::-1]

# Example usage:
if __name__ == "__main__":
    # Construct the n-ary tree for the first example
    root1 = Node(1, [
        Node(3, [Node(5), Node(6)]),
        Node(2),
        Node(4)
    ])
    
    solution = Solution()
    print(solution.postorder(root1))  # Output: [5, 6, 3, 2, 4, 1]
    
    # Construct the n-ary tree for the second example
    root2 = Node(1, [
        Node(2),
        Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
        Node(4, [Node(8, [Node(12)])]),
        Node(5, [Node(9, [Node(13)]), Node(10)])
    ])
    
    print(solution.postorder(root2))  # Output: [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
