# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=q=head
        while q.next:
            p=p.next 
            q=q.next.next
            if not q:
                return p
        return p