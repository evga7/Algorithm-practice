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
typedef vector<vector<pi>> gra;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int res;
int num;
int dp[101][101];
int m[101][101];
int T;
bool is_inside(int x, int y)
{
	if (x >= N || x < 0 || y < 0 || y >= N)return false;
	return true;
}
int solve(int x,int y)
{
	if (x == N - 1 && y == N - 1)return 1;
	if (!is_inside(x, y))return 0;
	int& ret = dp[x][y];
	if (ret!=-1)return ret;
	ret = 0;
	ret = max(solve(x, y + m[x][y]), solve(x + m[x][y], y));
	return ret;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> T;
	while (T--)
	{
		cin >> N;
		for (i = 0; i < N; i++)
			for (j = 0; j < N; j++)
				cin >> m[i][j];
		memset(dp, -1,sizeof(dp));
		if (solve(0,0))
			cout << "YES" << "\n";
		else
			cout << "NO" << "\n";
	}
}



