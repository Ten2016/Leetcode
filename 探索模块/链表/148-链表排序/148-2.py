# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # ∑Ω∑®£∫—°‘Ò≈≈–ÚO(n^2)
        length=0
        p=head
        while p:
            length+=1
            p=p.next
        p=head
        for i in range(length-1):
            k=q=p
            for j in range(length-i):
                if q.val<k.val:
                    k=q
                q=q.next
            p.val,k.val=k.val,p.val
            p=p.next
        return head