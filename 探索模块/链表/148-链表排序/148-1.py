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
        # 方法一：冒泡排序O(n^2)
        length=0
        p=head
        while p:
            length+=1
            p=p.next
        flag=True
        p=head
        for i in range(length-1):
            p=head
            for j in range(length-i-1):
                if p.val>p.next.val:
                    p.val,p.next.val=p.next.val,p.val
                    flag=False
                p=p.next
            if flag:
                break
        return head