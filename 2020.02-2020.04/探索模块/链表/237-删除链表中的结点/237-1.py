# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 此题是要移动结点的值
        p=node
        while p.next:
            p.val=p.next.val
            if p.next.next:
                p=p.next
            else:
                p.next=None
                return