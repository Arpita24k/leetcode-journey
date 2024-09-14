# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Initialize two pointers for both lists
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        # Traverse both lists
        while pA != pB:
            # If pA reaches the end of listA, switch it to the head of listB
            pA = pA.next if pA else headB
            # If pB reaches the end of listB, switch it to the head of listA
            pB = pB.next if pB else headA
        
        # Either they meet at the intersection, or both are None (no intersection)
        return pA
