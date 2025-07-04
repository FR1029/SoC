/* BST Node
class Node
{
   public:
    int data;
    Node *left;
    Node *right;

    Node(int x){
        data = x;
        left = NULL;
        right = NULL;
    }
}; */
class Solution {
  public:
    vector<Node*> findPreSuc(Node* root, int key) {
        Node* pre = NULL;
        Node* suc = NULL;
        Node* node = root;
        while (node) {
            if (node->data > key) {
                suc = node;
                node = node->left;
            } else node = node->right;
        }
        node = root;
        while (node) {
            if (node->data < key) {
                pre = node;
                node = node->right;
            } else node = node->left;
        }
        return {pre, suc};
    }
};