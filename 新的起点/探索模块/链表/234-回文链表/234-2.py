# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 反转链表后半段
        if not head or not head.next:
            return True
        p=q=head
        while q and q.next:
            p=p.next
            q=q.next.next
        # 如果长度为奇数，第二段多一个
        q=p.next
        p.next=None
        while q:
            c=q.next
            q.next=p
            p=q
            q=c
        q=head
        while p:
            if p.val!=q.val:
                return False
            p=p.next
            q=q.next
        return True