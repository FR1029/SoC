class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        int first = 0, second = 0;
        for (int i = 0; i < n; i++) {
            int third = max(first, second + nums[i]);
            second = first;
            first = third;
        }
        return first;
    }
};