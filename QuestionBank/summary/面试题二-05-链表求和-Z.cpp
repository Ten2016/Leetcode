>>:题目描述：
给定两个用链表表示的整数，每个节点包含一个数位。
这些数位是反向存放的，也就是个位排在链表首部。
编写函数对这两个整数求和，并用链表形式返回结果。


示例：
输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912

进阶：假设这些数位是正向存放的，请再做一遍。

示例：
输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-lists-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

>>:解法：
略

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