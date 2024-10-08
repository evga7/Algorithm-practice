#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000009
#define pb push_back
#define pob pop_back
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
int res;
int num, num2;
int T;
int S;
vec v;
vec v2;
int dp[1000001];
int solve(int idx)
{
	if (idx == 0)return 1;
	int& ret = dp[idx];
	if (ret != -1)return ret;
	int i;
	ret = 0;
	for (i = 1; i <= 3; i++)
	{
		ret += solve(idx - i);
		ret %= MOD;
	}
	return ret%MOD;
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
		cout << solve(N)%MOD<<"\n";
	}
}




