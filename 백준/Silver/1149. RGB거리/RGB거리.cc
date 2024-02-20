#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000009
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
ll dp[1001][3];
ll res = MAX;
ll arr[1001][4];
ll go(int idx,int pos)
{
	if (idx == N)
		return 0;
	ll& ret = dp[idx][pos];
	if (ret != -1)return ret;
	ret = 987654321;
	for (int i = 0; i < 3; i++)
	{
		if (i == pos)continue;
		ret = min(ret, go(idx + 1, i) + arr[idx][i]);
	}
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
	for (int i = 0; i < N; i++)
	{
		cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
	}
	for (int i = 0; i < 3; i++)
		res = min(res, go(1, i)+arr[0][i]);
	cout << res;
}

