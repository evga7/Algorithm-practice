#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
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
int dp[11];
int T;
int solve(int idx)
{
	if (idx < 0)return 0;
	if (idx == 0)
		return 1;
	int& ret = dp[idx];
	if (ret != -1)
		return ret;
	ret = 0;
	ret += solve(idx - 1);
	ret += solve(idx - 2);
	ret += solve(idx - 3);
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> T;
	memset(dp, -1, sizeof(dp));
	while (T--)
	{
		cin >> N;
		cout << solve(N)<<"\n";
	}
}

