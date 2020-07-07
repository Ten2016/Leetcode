>>:题目描述：
编写一个函数，检查输入的链表是否是回文的。


示例 1：
输入： 1->2
输出： false

示例 2：
输入： 1->2->2->1
输出： true 
 

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list-lcci
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
    bool isPalindrome(ListNode* head) {
        vector<int> vec;
        ListNode *p = head;
        while(p){
            vec.push_back(p->val);
            p = p->next;
        }
        int i=0, j=vec.size()-1;
        while(i<j && vec[i]==vec[j]){
            i++;
            j--;
        }
        return i>=j;
    }
};