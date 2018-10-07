# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=q=head
        f=False
        while q and q.next:
            p=p.next
            q=q.next.next
            if p==q:
                f=True
                break
        if f:
            p=head
            while p!=q:
                p=p.next
                q=q.next
            return p
        else:
            return None