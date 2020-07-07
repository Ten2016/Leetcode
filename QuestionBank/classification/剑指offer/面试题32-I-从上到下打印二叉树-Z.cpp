>>:题目描述：
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

>>:解法：
略

>>:程序：

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> levelOrder(TreeNode* root) {
        if(root == nullptr) return vector<int>(0);
        vector<int> ans;
        queue<TreeNode*> que;
        que.push(root);
        while(!que.empty()){
            TreeNode *p = que.front();
            que.pop();
            ans.push_back(p->val);
            if(p->left) que.push(p->left);
            if(p->right) que.push(p->right);
        }
        return ans;
    }
};