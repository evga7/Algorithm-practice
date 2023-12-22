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
ll res;
int num, num2;
string str;
ll dp[11][2001];
ll solve(int idx, int pos)
{
	if (idx == 1)
		return 1;
	ll& ret = dp[idx][pos];
	if (ret != -1)
		return ret;
	ret = 0;
	for (int i = pos / 2; i >= 1; i--)
		ret += solve(idx - 1, i);
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> T;
	while (T)
	{
		cin >> N >> M;
		T -= 1;
		memset(dp, -1, sizeof(dp));
		res = 0;
		for (int i = M; i >= 1; i--)
			res += solve(N, i);
		cout << res << "\n";

	}
}