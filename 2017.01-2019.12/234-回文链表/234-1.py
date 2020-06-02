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
        # 使用n个额外空间
        lst=[]
        p=head
        while p:
            lst.append(p.val)
            p=p.next
        p,q=0,len(lst)-1
        while p<q:
            if lst[p]!=lst[q]:
                return False
            p+=1
            q-=1
        return True