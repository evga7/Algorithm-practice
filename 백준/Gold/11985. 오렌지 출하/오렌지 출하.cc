#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int N, M, K;
vector<int> a;
vector<long long> dp;

long long go(int idx) {
    if (idx == N) {
        return 0;
    }
    if (dp[idx] != -1) {
        return dp[idx];
    }

    long long ret = LLONG_MAX;
    int mi = a[idx];
    int mx = a[idx];
    for (int i = idx; i < min(idx + M, N); ++i) {
        mx = max(mx, a[i]);
        mi = min(mi, a[i]);
        long long su = mx - mi;
        long long num = i - idx + 1;
        ret = min(ret, go(i + 1) + (K + num * su));
    }

    dp[idx] = ret;
    return dp[idx];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M >> K;
    a.resize(N);
    dp.resize(N + 1, -1);

    for (int i = 0; i < N; ++i) {
        cin >> a[i];
    }

    cout << go(0) << endl;

    return 0;
}
