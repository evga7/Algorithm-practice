#include <bits/stdc++.h>
#define MAX 2147483647
#define MIN -2147483648
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
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int num;
ll res;
ll dp[101][10];
ll solve(int idx, int cnt)
{
	if (idx == N) return 1;
	ll& ret = dp[idx][cnt];
	if (ret!=-1) return ret;
	if (cnt == 0)
		return ret = solve(idx + 1, cnt + 1) % MOD;
	else if (cnt == 9)
		return ret = solve(idx + 1, cnt - 1) % MOD;
	else
		return ret = (solve(idx + 1, cnt - 1) + solve(idx+1, cnt + 1)) % MOD;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	memset(dp, -1, sizeof(dp));
	for (i = 1; i <= 9; i++)
		res += solve(1, i) % MOD;
	cout << res%MOD;
}
