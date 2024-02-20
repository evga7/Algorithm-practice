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
int N, M;
ll res;
int num, num2;
int T;
int K;
ll dp[201][201];
vec2 v;
ll solve(int n, int k)
{
	if (k == K)
	{
		if (n== N)return 1;
		return 0;
	}
	ll& ret = dp[n][k];
	if (ret != -1)return ret;
	ret = 0;
	int i;
	for (i = N; i>=n; i--)
	{
		ret += solve(i, k + 1);
		ret %= MOD;
	}
	return ret;
}
int main()
{ 
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> K;
	memset(dp, -1, sizeof(dp));
	cout << solve(0, 0);
}



