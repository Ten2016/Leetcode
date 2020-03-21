# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length=0
        p=head
        while p:
            length+=1
            p=p.next
        if n==length:
            head=head.next
        else:
            p=head
            for i in range(length-n-1):
                p=p.next
            p.next=p.next.next
        return head