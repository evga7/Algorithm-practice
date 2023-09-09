#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000000
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
int dx[4] = { 0,1,0,-1 };//왼 아 오 위
int dy[4] = { -1,0,1,0 };
ll N, M, T;
int L;
int num;
int V, E, K;
vec v;
int dp[5001][5001];
int solve(int idx,int cnt)
{
    if (idx == 0 || cnt == 1)
        return 1;
    int& ret = dp[idx][cnt];
    if (ret != -1)
        return ret;
    return ret = (solve(idx - 1, cnt) + solve(idx, cnt - 1)) % MOD;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    memset(dp, -1, sizeof(dp));
    cout << solve(N,M);

}
