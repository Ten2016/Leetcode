>>:题目描述：
给出两个非空链表用来表示两个非负的整数。
其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


>>:解法：
两个链表按位相加即可，不过在加的过程中需要模拟进位的情况。
在最后需要考虑最高位还有进位的特殊情况。


>>:程序：

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *p = l1;
        ListNode *q = l2;
        ListNode *head = new ListNode(0);
        ListNode *t = head;
        int c = 0;
        while(p && q){
            t->next = new ListNode((p->val + q->val + c)%10);
            t = t->next;
            c = (p->val + q->val + c)/10;
            p = p->next;
            q = q->next;
        }
        while(p){
            t->next = new ListNode((p->val + c)%10);
            t = t->next;
            c = (p->val + c)/10;
            p = p->next;         
        }
        while(q){
            t->next = new ListNode((q->val + c)%10);
            t = t->next;
            c = (q->val + c)/10;
            q = q->next;           
        }
        if(c){
            t->next = new ListNode(c); 
            t = t->next;
        }     
        t->next = NULL;
        return head->next;
    }
};