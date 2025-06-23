class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        int first1 = 0, second1 = 0, first2 = 0, second2 = 0;
        for (int i = 0; i < n - 1; i++) {
            int third = max(first1, second1 + nums[i]);
            second1 = first1;
            first1 = third;
        }
        for (int i = 1; i < n; i++) {
            int third = max(first2, second2 + nums[i]);
            second2 = first2;
            first2 = third;
        }
        first1 = max(first1, nums[0]);
        return max(first1, first2);
    }
};