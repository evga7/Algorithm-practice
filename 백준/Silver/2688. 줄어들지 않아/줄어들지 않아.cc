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
ll res;
int num, num2;
int T;
int S;
vec v;
ll dp[1001][10];
ll solve(int n, int m)
{
	if (n == 1) return 1;
	ll& ret = dp[n][m];
	if (ret != -1)return ret;
	ret = 0;
	for (int i = m; i <= 9; i++)
	{
		ret += solve(n-1, i);
	}
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> T;
	memset(dp, -1, sizeof(dp));
	while (T--)
	{
		cin >> N;
		res = 0;
		for (int i=0;i<=9;i++)
			res+=solve(N,i);
		cout << res<<"\n";
	}
	
}




