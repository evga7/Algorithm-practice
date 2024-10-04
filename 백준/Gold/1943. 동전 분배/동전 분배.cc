#include<bits/stdc++.h>// memset 사용을 위해 필요
using namespace std;

const int MAX = INT_MAX;
const int MOD = 1e9+7;

int dp[100][100001];  // dp 배열 선언
vector<pair<int, int>> a;
int N;

// 재귀 함수
int go(int idx, int cnt) {
    if (idx == N) {
        return cnt == 0 ? 1 : 0;
    }
    if (dp[idx][cnt] != -1) {
        return dp[idx][cnt];
    }
    
    int ret = 0;
    for (int i = 1; i <= a[idx].second; ++i) {
        if (cnt - (a[idx].first * i) >= 0) {
            ret = max(ret, go(idx + 1, cnt - (a[idx].first * i)));
        }
    }
    ret = max(ret, go(idx + 1, cnt));
    dp[idx][cnt] = ret;
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    while (true) {
        if (!(cin >> N)) break;  // 입력이 더 이상 없으면 종료
        
        a.resize(N);
        int s = 0;
        memset(dp, -1, sizeof(dp));  // dp 배열을 -1로 초기화
        
        for (int i = 0; i < N; ++i) {
            cin >> a[i].first >> a[i].second;
            s += a[i].first * a[i].second;
        }
        
        int res = 0;
        if (s % 2 == 0) {
            res = go(0, s / 2);
        }
        
        cout << res << "\n";
    }
    
    return 0;
}
