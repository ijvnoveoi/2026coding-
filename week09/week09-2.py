#week09-2.py
a = []
while head:
    a.append( head.val )
    head = head.next
now = ans = ListNode()
N = len(a)
for i in range(N-1, -1, -1):
    now.next = ListNode(a[i])
    now = now.next
        return ans.next
