#include <bits/stdc++.h>
#define MAX 1000000001
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, pair<int, int>>pi2;
int dx[4] = { 0,-1,0,1 };
int dy[4] = {-1,0,1,0 };
int N,M;
int arr[501][501];
int visited[501][501];
int res = 0;
void solve(int x,int y,int cnt, int sum)
{
	if (cnt == 3)
	{
		res = max(res, sum);
		return;
	}
	int i;
	for (i = 0; i < 4; i++)
	{
		int n_x = x + dx[i];
		int n_y = y + dy[i];
		if (n_x < 0 || n_x >= N || n_y < 0 || n_y >= M||visited[n_x][n_y])continue;
		visited[n_x][n_y] = 1;
		solve(n_x, n_y, cnt + 1, sum + arr[n_x][n_y]);
		visited[n_x][n_y] = 0;
	}
	return;
}
void chk(int x, int y)
{
	if (!(y - 1 < 0 || y + 1 >= M || x + 1 >= N))//ㅜ모양
		res = max(res, arr[x][y - 1] + arr[x][y] + arr[x][y + 1] + arr[x + 1][y]);

	if (!(y - 1 < 0 || x + 1 >=N || x -1 <0))//ㅓ모양
		res = max(res, arr[x][y - 1] + arr[x][y] + arr[x+1][y] + arr[x-1][y]);

	if (!(y - 1 < 0 || y+ 1 >= M || x - 1 < 0))//ㅗ모양
		res = max(res, arr[x][y - 1] + arr[x][y] + arr[x][y+1] + arr[x - 1][y]);

	if (!(x - 1 < 0 || x + 1 >= N || y+ 1>=M))//ㅏ모양
		res = max(res, arr[x-1][y] + arr[x][y] + arr[x + 1][y] + arr[x][y+1]);
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i,j;
	int num;
	cin >> N>>M;
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < M; j++)
		{
			cin >> arr[i][j];
		}
	}
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < M; j++)
		{
			visited[i][j] = 1;
			solve(i, j,0,arr[i][j]);
			chk(i, j);
			visited[i][j] = 0;
		}
	}
	cout << res;
}

