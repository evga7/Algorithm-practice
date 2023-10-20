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
ll N, M;
int T;
int K;
int res;
int num, num2;
string str;
vector<vector<pair<int, int>>>v;
int a[11][11];
int visited[11][11];
int p[101];
int pos = 1;
typedef struct info {
	int cnt, x, y, n_x, n_y;
}info;
vector<info>connect_v;
bool is_inside(int x, int y, int N, int M)
{
	return 0 <= x && x < N && 0 <= y && y < M;
}
int find(int x)
{
	if (x == p[x])
		return x;
	return p[x] = find(p[x]);
}
bool cmp(const info& i1, const info& i2)
{
	return i1.cnt < i2.cnt;
}
bool uni(int x, int y)
{
	x = find(x);
	y = find(y);
	if (x != y)
	{
		if (x < y)
			p[y] = x;
		else
			p[x] = y;
		return true;
	}
	return false;
}
void go(int sx, int sy)
{
	queue<pair<int, int>>q;
	q.push(make_pair(sx, sy));
	visited[sx][sy] = pos;
	while (!q.empty())
	{
		auto cur = q.front();
		q.pop();
		int x, y;
		x = cur.first;
		y = cur.second;
		v[pos].push_back(make_pair(x, y));
		for (int i = 0; i < 4; i++)
		{
			int n_x = x + dx[i];
			int n_y = y + dy[i];
			if (is_inside(n_x, n_y, N, M) && a[n_x][n_y] && !visited[n_x][n_y])
			{
				visited[n_x][n_y] = pos;
				q.push({ n_x,n_y });
			}
		}
	}
}
void go2(int sx, int sy, int op,int val)
{
	int cnt = 0;
	int x = sx;
	int y = sy;
	while (1)
	{
		int n_x = x + dx[op];
		int n_y = y + dy[op];
		if (!is_inside(n_x, n_y, N, M))return;
		if (a[n_x][n_y])
		{
			if (visited[n_x][n_y] != val && cnt > 1)
				connect_v.push_back({ cnt,sx,sy,n_x,n_y });
			return;
		}
		cnt += 1;
		x = n_x;
		y = n_y;
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M;
	v.resize(101);
	for (int i = 1; i <= 101; i++)
		p[i] = i;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> a[i][j];
		}
	}
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (a[i][j] && !visited[i][j])
			{
				go(i, j);
				pos += 1;
			}
		}
	}
	for (int i = 1; i < pos; i++)
	{
		for (auto cur : v[i])
		{
			int x = cur.first;
			int y = cur.second;
			for (int j=0;j<4;j++)
				go2(x, y,j,i);
		}
	}
	sort(connect_v.begin(), connect_v.end(),cmp);
	for (auto cur : connect_v)
	{
		if (uni(visited[cur.x][cur.y], visited[cur.n_x][cur.n_y]))
		{
			res += cur.cnt;
		}
	}
	int cc = find(1);
	for (int i = 2; i < pos; i++)
	{
		if (cc != find(i))
		{
			cout << -1;
			exit(0);
		}
	}
	cout << res;

}





