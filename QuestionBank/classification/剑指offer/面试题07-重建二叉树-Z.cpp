>>:题目描述：
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

限制：
0 <= 节点个数 <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.size()==0)
            return nullptr;
        TreeNode *root;
        root = func(preorder, inorder, 0, 0, inorder.size()-1);

        return root;
    }

private:
    TreeNode* func(vector<int>& preorder, vector<int>& inorder, int preroot, int inleft, int inright){
        if(inleft>inright)
            return nullptr;
        TreeNode *root = new TreeNode(preorder[preroot]);
        int inroot=inleft;
        while(inroot<=inright && preorder[preroot]!=inorder[inroot]) 
            ++inroot;
        root->left  = func(preorder,inorder,preroot+1,inleft,inroot-1);
        preroot += inroot-inleft+1;
        root->right = func(preorder,inorder,preroot,inroot+1,inright);

        return root;
        
    }
};