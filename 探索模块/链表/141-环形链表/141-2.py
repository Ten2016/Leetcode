# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dit={}
        q=head
        while q:
            if q not in dit:
                dit[q]=1
            else:
                return True
            q=q.next
        return False