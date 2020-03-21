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
        n=0
        p=head
        while p.next:
            n+=1
            p=p.next
        
        n=(n+1)>>1
        p=head
        for i in range(n):
            p=p.next
        return p