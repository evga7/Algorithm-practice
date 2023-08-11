#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 0x3f3f3f3f
#define MIN -987654321
#define MOD  1000000009
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
int dx[4] = { 0,1,0,-1 };//왼 아 오 위
int dy[4] = { -1,0,1,0 };
ll N, M, T;
int L;
int num;
int V, E, K;
vec v;
int dp[1001][1000][4];
int res = MAX;
int arr[1001][1001];
bool is_inside(int x, int y, int N, int M)
{
	return 0 <= x && x < N && 0 <= y && y < M;
}
int solve(int x, int y,int dir)
{
	if (x == N-1) return arr[x][y];
	int& ret = dp[x][y][dir];
	if (ret != MAX)
		return ret;
	for (int i = 0; i < 3; i++)
	{
		if (dir == i)continue;
		int n_x = x + 1;
		int n_y = y + dy[i];
		if (is_inside(n_x,n_y,N,M))
		{
			ret = min(ret, solve(n_x, n_y,i) + arr[x][y]);
		}
		
	}
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> arr[i][j];
		}
	}
	memset(dp, MAX, sizeof(dp));
	for (int i = 0; i < M; i++)
	{
		res = min(res, solve(0, i,3));
	}
	cout << res;
}
