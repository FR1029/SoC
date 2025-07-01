/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int diameter = 0;
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        int right = maxDepth(root -> right);
        int left = maxDepth(root -> left);
        diameter = max(diameter, left + right);
        return 1 + max(left, right);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        maxDepth(root);
        return diameter;
    }
};