#include <bits/stdc++.h>
#define MAX 2147483647
#define MIN -2147483648
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
int res;
int num;
int arr[501][501];
int dp[501][501];
bool is_inside(int x, int y)
{
	if (x >= N || x < 0 || y < 0 || y >= M)return false;
	return true;
}
int solve(int x, int y)
{
	int& ret = dp[x][y];
	if (x==N-1&&y==M-1)return 1;
	if (ret != -1)return ret;
	ret = 0;
	int i;
	for (i = 0; i < 4; i++)
	{
		int n_x = x + dx[i];
		int n_y = y + dy[i];
		if (arr[x][y] <= arr[n_x][n_y] || !is_inside(n_x, n_y))continue;
		ret += solve(n_x, n_y);
	}
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	for (i = 0; i < N; i++)
		for (j = 0; j < M; j++)
			cin >> arr[i][j];
	memset(dp, -1, sizeof(dp));
	cout << solve(0, 0);
}



