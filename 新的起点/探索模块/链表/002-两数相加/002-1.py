# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, p1, p2= ListNode(-1), l1, l2
        tail = head #尾结点
        carry = 0;  #进位
        while p1 and p2:
            num = p1.val + p2.val + carry
            if num > 9:
                num -= 10
                carry = 1
            else:
                carry = 0
            # 添加结点
            tail.next = ListNode(num)
            tail = tail.next
            # 移动两条链
            p1 = p1.next
            p2 = p2.next
        # 取两条链长的那条剩下的部分
        if p2: 
            p1 = p2
        while p1:
            num = p1.val + carry
            if (num > 9):
                num -= 10
                carry = 1
            else:
                carry = 0
            
            tail.next = ListNode(num)
            tail = tail.next
            
            p1 = p1.next
        # 如果最后还有进位，再分配一个结点
        if carry:
            tail.next = ListNode(1)
            tail = tail.next
        tail.next = None    # 将链表收尾
        return head.next    #去掉空的头结点

        
                
        