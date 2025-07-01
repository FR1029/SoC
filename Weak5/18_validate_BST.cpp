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
    bool isValidBST(TreeNode* root) {
        stack<tuple<TreeNode*, long, long>> st;
        st.push({root, LONG_MIN, LONG_MAX});
        while (!st.empty()) {
            auto [node, lower, upper] = st.top();
            st.pop();
            if (!node) continue;
            if (node->val <= lower || node->val >= upper)
                return false;

            st.push({node->right, node->val, upper});
            st.push({node->left, lower, node->val});
        }
        return true;
    }
};