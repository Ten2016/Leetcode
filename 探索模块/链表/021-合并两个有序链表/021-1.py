# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 初始化
        if not l1 and not l2:
            return None
        elif l1 and l2:
            if l1.val<=l2.val:
                res=l1
                p,q=l1,l2
            else:
                res=l2
                q,p=l1,l2
        elif l1 and not l2:
            res=l1
            p,q=l1,l2
        else:
            res=l2
            q,p=l1,l2
        # 开始
        while q:
            if q.val>=p.val:
                if p.next:
                    if q.val>=p.next.val:
                        p=p.next
                    else:
                        if q.next:
                            s=q.next
                            q.next=p.next
                            p.next=q
                            q=s
                            p=p.next
                        else:
                            q.next=p.next
                            p.next=q
                            break
                else:
                    p.next=q
                    break
            else:
                p=p.next
        return res