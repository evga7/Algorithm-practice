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
typedef vector<vector<pi>> gra;
//int dx[4] = { 0,0,-1,1 };
//int dy[4] = { 1,-1,0,0 };
const int dy[9] = { -1,0,1,1,1,0,-1,-1,0 };
const int dx[9] = { 1,1,1,0,-1,-1,-1,0,0 };
int N, M;
int T;
int K;
int res;
int num, num2;
string str;
int visited[9][9][9];
char m[9][9];
bool is_inside(int x, int y)
{
	return x >= 0 && x < N&& y >= 0 && y < M;
}

int solve()
{
	queue<pi2>q;
	q.push({ 0,{ 7,0 } });
	visited[0][7][0] = 1;
	while (!q.empty())
	{

		int cnt = q.front().first;
		int x = q.front().second.first;
		int y = q.front().second.second;
		if (x == 0 && y == 7)return 1;
		q.pop();
		for (int i = 0; i < 9; i++)
		{
			int n_x = x + dx[i];
			int n_y = y + dy[i];
			int n_cnt = min(cnt + 1, 8);
			if (!is_inside(n_x, n_y))continue;
			if (n_x - cnt >= 0 && m[n_x - cnt][n_y] == '#')continue;
			if (n_x - cnt-1 >= 0 && m[n_x - cnt-1][n_y] == '#')continue;
			if (!visited[n_cnt][n_x][n_y])
			{
				visited[n_cnt][n_x][n_y] = 1;
				q.push({ n_cnt,{ n_x,n_y } });
			}
		}
	}
	return 0;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	N = M = 8;
	for (i = 0; i < 8; i++)
	{
		for (j = 0; j < 8; j++)
		{
			cin >> m[i][j];
		}
	}
	cout<<solve();
}





