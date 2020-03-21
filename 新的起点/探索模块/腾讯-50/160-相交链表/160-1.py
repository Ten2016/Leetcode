# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1=len2=0
        if not headA or not headB:
            return None
        p,q=headA,headB
        while p.next:
            p=p.next
            len1+=1
        while q.next:
            q=q.next
            len2+=1
        if p==q:
            p,q=headA,headB
            if len1<len2:
                for i in range(len2-len1):
                    q=q.next
            else:
                for i in range(len1-len2):
                    p=p.next
            while p!=q:
                p=p.next
                q=q.next
            return p
        else:
            return None