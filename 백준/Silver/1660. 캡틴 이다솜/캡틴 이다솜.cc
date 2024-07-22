#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

const int MOD = 1000000009;
const int INF = 987654321;

int N;
vector<int> a;
vector<int> dp;

int go(int idx) {
    if (idx == 0) return 0;
    if (dp[idx] != -1) return dp[idx];
    
    int ret = INF;
    for (int i = 0; i < a.size(); ++i) {
        int cur = a[i];
        if (idx < cur) break;
        ret = min(ret, go(idx - cur) + 1);
    }
    
    dp[idx] = ret;
    return dp[idx];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;

    int s = 1;
    int num = 2;
    a.push_back(1);
    
    while (num <= N + 1) {
        s += num;
        num++;
        a.push_back(s + a.back());
    }
    
    dp = vector<int>(N + 1, -1);
    
    cout << go(N) << "\n";
    
    return 0;
}
