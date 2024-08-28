from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # Initialize a queue for level order traversal
        queue = deque([root])
        
        while queue:
            size = len(queue)
            prev = None
            
            for i in range(size):
                node = queue.popleft()
                
                # If there's a previous node at this level, set its next to the current node
                if prev:
                    prev.next = node
                prev = node
                
                # Add left and right children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # The last node in this level should point to None
            prev.next = None
        
        return root

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    
    # Constructing the binary tree from the example
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    
    # Connecting nodes
    connected_root = solution.connect(root)
    
    # This function can be used to visualize the level order next pointers
    def print_levels(root):
        while root:
            current = root
            while current:
                print(current.val, end=" -> ")
                current = current.next
            print("#")  # End of level
            root = root.left

    print_levels(connected_root)
    # Expected output:
    # 1 -> #
    # 2 -> 3 -> #
    # 4 -> 5 -> 7 -> #
