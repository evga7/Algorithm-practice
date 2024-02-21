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
ll res=987654321;
vec v;
int num;
ll dp[1001][3][3];
int arr[1001][3];
bool is_inside(int x, int y, int N, int M)
{
	return 0 <= x && x < N && 0 <= y && y < M;
}
ll go(int x,int y,int start)
{
	if (x == N)
	{
		if (y != start)
			return arr[x][y];
		return 987654321;
	}
	ll& ret = dp[x][y][start];
	if (ret != -1)
		return ret;
	ret = 987654321;
	for (int i = 0; i < 3; i++)
	{
		if (i != y)
		{
			ret = min(ret, go(x + 1, i, start) + arr[x][i]);
		}
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
		cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
	for (int i = 0; i < 3; i++)
		res = min(res, go(1, i, i)+arr[0][i]);
	cout << res;
}

