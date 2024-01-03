# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv, nxt = head, head.next
        while nxt:
            new_val = math.gcd(prv.val, nxt.val)
            new_node = ListNode(new_val)
            prv.next, new_node.next = new_node, nxt
            prv = nxt
            nxt = nxt.next
        return head