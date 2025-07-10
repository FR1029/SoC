class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<vector<pair<int, int>>> graph(n);
        for (auto& flight : flights) {
            graph[flight[0]].emplace_back(flight[1], flight[2]);
        }
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
        pq.emplace(0, src, 0);
        vector<int> visited(n, INT_MAX);
        while (!pq.empty()) {
            auto [cost, u, stops] = pq.top();
            pq.pop();
            if (u == dst) return cost;
            if (stops > k || stops > visited[u]) continue;
            visited[u] = stops;
            for (auto [v, price] : graph[u]) {
                pq.emplace(cost + price, v, stops + 1);
            }
        }
        return -1;
    }
};