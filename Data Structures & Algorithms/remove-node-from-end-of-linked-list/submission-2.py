# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# We use two pointers slow and fast. The fast pointer gets a lead of n steps 
# There is always a gap of n between them so we just remove the next node of slow

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        dummy.next = head

        slow = dummy
        fast = dummy

        for i in range(n+1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next