# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        b=head
        c=head.next
        head.next=None
        while c:
            a=c.next
            c.next=b
            b=c
            c=a
        return b