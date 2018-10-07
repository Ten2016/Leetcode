# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 考察链表反转
        # 向右移动则反转点定位在又数第k个
        length=0
        p=head
        while p:
            length+=1
            p=p.next
        if k==0 or length==0 or length==1 or k%length==0:
            return head
        # 计算移动的步数
        k=length-k%length
        # 将前k个数反转
        p,q=head,head.next
        n=1
        while q and n<k:
            c=q.next
            q.next=p
            p=q
            q=c
            n+=1
        # 将后半段反转
        res=p   #第一段的头
        tmp=q   #第二段的尾
        while q:
            c=q.next
            q.next=p
            p=q
            q=c
        head.next=p     #第一段的尾接第二段的头
        tmp.next=None   #第二段的尾置为None
        # 将整个链表反转
        p,q=res,res.next
        while q:
            c=q.next
            q.next=p
            p=q
            q=c
        res.next=None
        return p