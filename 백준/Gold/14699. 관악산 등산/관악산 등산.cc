#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000009
#define pb push_back
#define pob pop_back
#define ms memset
#define FOR(i,a,b) for(int i = a; i < b; i++)
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef tuple<int, int, int> tup;
typedef vector<vector<pi>> gra;
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };
int N, M;
int T;
int K;
int res;
int num, num2;
string str;
int h[5001];
vvec v;
int dp[5001];
int visited[5001];
int solve(int idx)
{
	int& ret = dp[idx];
	if (ret != -1)return ret;
	ret = 1;
	for (auto next : v[idx])
	{
		ret = max(ret, solve(next) + 1);
	}
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M;
	for (int i = 1; i <= N; i++)
	{
		cin >> h[i];
	}
	int a, b;
	v.resize(N + 1);
	for (int i = 0; i < M; i++)
	{
		cin >> a >> b;
		if (h[a] > h[b])
			v[b].push_back(a);
		else if (h[a]<h[b])
			v[a].push_back(b);
	}
	memset(dp, -1, sizeof(dp));
	for (int i = 1; i <= N; i++)
		cout << solve(i) << "\n";
}