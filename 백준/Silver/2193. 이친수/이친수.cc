#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000000
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vpi;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef vector<vector<pi>> gra;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M, T;
ll dp[91][2];
int arr[100001];
vec v;
ll solve(int idx,int cnt)
{
	if (idx == 1)return 1;
	ll& ret = dp[idx][cnt];
	if (ret != -1)return ret;
	ret = 0;
	if (cnt == 0)
		ret += solve(idx - 1, 1);
	ret += solve(idx - 1, 0);
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	memset(dp, -1, sizeof(dp));
	ll res = 0;
	cout << solve(N,1);
	
}
