#include <bits/stdc++.h>
using namespace std;

bool f(int ind, int k, vector<int> &arr, vector<vector<int>> &dp) {
    if (k == 0) return true;
    if (ind == 0) return arr[0] == k;

    if (dp[ind][k] != -1) return dp[ind][k];

    bool notTake = f(ind - 1, k, arr, dp);
    bool take = false;
    if (arr[ind] <= k) {
        take = f(ind - 1, k - arr[ind], arr, dp);
    }

    dp[ind][k] = take || notTake;
    return dp[ind][k];
}

bool subsetSumToK(int n, int k, vector<int> &arr) {
    vector<vector<int>> dp(n, vector<int>(k + 1, -1));
    return f(n - 1, k, arr, dp);
}
