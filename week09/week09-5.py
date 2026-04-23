#week09-5.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return None
        prev = fast = slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        #print(slow.val)
        prev.next = slow.next
        return head
