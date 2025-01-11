#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
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
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };
int N, M;
int L, R;
int T;
int res;
int num, num2;
int sum;
string str;
vec2 v;
int m[51][51];
int c[51][51];
int visited[51][51];
vec2 air;
vec2 munji;
void copy_map()
{
	int i, j;
	for (i = 0; i < N; i++)
		for (j = 0; j < M; j++)
			m[i][j] += c[i][j];
}
bool is_inside(int x, int y)
{
	return x >= 0 && x < N&& y >= 0 && y < M;
}
void solve(int x, int y)
{
	int cost = m[x][y] / 5;
	int cnt = 0;
	for (int i = 0; i < 4; i++)
	{
		int n_x = x + dx[i];
		int n_y = y + dy[i];
		if (!is_inside(n_x, n_y) || m[n_x][n_y] == -1)continue;
		cnt++;
		c[n_x][n_y] += cost;
	}
	m[x][y] -= cost * cnt;
}
void wind_up(int X, int Y)
{
	int x = X-1;
	int y = Y;
	while (x >=0)
	{
		if (m[x + 1][y] == -1)
			m[x][y] = 0;
		else
			m[x + 1][y] = m[x][y];
		x--;
	}
	x = 0;
	y = 1;
	while (y <M)
	{
		m[x][y - 1] = m[x][y];
		y++;
	}
	x++;
	y--;
	while (x <=X)
	{
		m[x-1][y] = m[x][y];
		x++;
	}
	x = X;
	y--;
	while (y>Y)
	{
		m[x][y + 1] = m[x][y];
		y--;
	}
	m[x][y+1] = 0;
}
void wind_down(int X, int Y)
{
	int x = X + 1;
	int y = Y;
	m[x][y] = 0;
	x++;
	while (x<N)
	{
		m[x - 1][y] = m[x][y];
		x++;
	}
	x--;
	y = 1;
	while (y < M)
	{
		m[x][y - 1] = m[x][y];
		y++;
	}
	y--;
	m[x][y] = 0;
	while (x >=X)
	{
		m[x + 1][y] = m[x][y];
		x--;
	}
	x = X;
	while (y > Y)
	{
		m[x][y + 1] = m[x][y];
		y--;
	}
	m[x][y + 1] = 0;

}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M >> T;
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < M; j++)
		{
			cin >> m[i][j];
			if (m[i][j] == -1)
				air.pb({ i,j });
		}
	}
	int t = 0;
	while (1)
	{
		t++;
		
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < M; j++)
			{
				if (m[i][j] > 0)
					munji.push_back({ i,j });
			}
		}
		for (auto next : munji)
		{
			solve(next.first, next.second);
		}
		copy_map();
		wind_up(air[0].first, air[0].second);
		wind_down(air[1].first, air[1].second);
		if (t == T)break;
		munji.clear();
		memset(c, 0, sizeof(c));
	}
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < M; j++)
		{
			if (m[i][j] > 0)
				res += m[i][j];
		}
}
	cout << res;

}






