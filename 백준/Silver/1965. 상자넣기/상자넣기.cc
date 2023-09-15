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
int N, M, T;
int num;
bool is_inside(int x, int y)
{
    return 0 <= x && x < N && 0 <= y && y < M;
}
int V, E, K;
string s;
int res;
vector<int>v;
int dp[1001];
int solve(int idx)
{
    int& ret = dp[idx];
    if (ret != -1)
        return ret;
    ret = 1;
    for (int i = idx; i < N; i++)
    {
        if (v[idx] < v[i])
            ret = max(ret, solve(i) + 1);
    }
    return ret;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i < N; i++)
    {
        cin >> num;
        v.push_back(num);
    }
    for (int i = 0; i < N; i++)
        res = max(res, solve(i));
    cout << res;
    
}

