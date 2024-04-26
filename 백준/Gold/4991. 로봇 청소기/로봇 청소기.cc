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
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };
int N, M;
int T;
int K;
int res;
int num, num2;
char m[21][21];
bool visited[21][21];
int dist[21][21];
bool chk[1001];
deque<pi> dq;
bool is_inside(int x, int y)
{
	return x >= 0 && x < N&& y >= 0 && y < M;
}
struct info {
	int x, y, dist;
};
int solve(int X,int Y,int ex,int ey)
{
	queue<info>q;
	q.push({ X,Y,0 });
	memset(visited, 0, sizeof(visited));
	visited[X][Y] = 1;
	while (!q.empty())
	{
		int x = q.front().x;
		int y = q.front().y;
		int dist = q.front().dist;
		q.pop();
		if (x == ex && y == ey)
			return dist;
		for (int i = 0; i < 4; i++)
		{
			int n_x = x + dx[i];
			int n_y = y + dy[i];
			if (!is_inside(n_x, n_y) || visited[n_x][n_y]||m[n_x][n_y]=='x')continue;
			visited[n_x][n_y] = 1;
			q.push({ n_x,n_y,dist + 1 });
		}
	}
	return 0;
}
void dfs(int idx,int sum,int cnt)
{
	if (cnt == dq.size()-1)
	{
		res = min(sum, res);
		return;
	}
	for (int i = 1; i < dq.size(); i++)
	{
		if (!chk[i]&&dist[idx][i])
		{
			chk[i] = 1;
			dfs(i, sum + dist[idx][i], cnt + 1);
			chk[i] = 0;
		}
	}

}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	while (1)
	{
		cin >> M >> N;
		memset(chk, 0, sizeof(chk));
		memset(dist, 0, sizeof(dist));
		if (N == 0 && M == 0)break;
		dq.clear();
		res = MAX;
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < M; j++)
			{
				cin >> m[i][j];
				if (m[i][j] == 'o')
					dq.push_front({ i,j });
				else if (m[i][j] == '*')
				{
					dq.pb({ i,j });
				}
			}
		}
		for (i = 0; i < dq.size(); i++)
		{
			for (j = i + 1; j < dq.size(); j++)
			{
				if (dist[i][j] || dist[j][i])continue;
				int x = dq[i].first;
				int y = dq[i].second;
				int ex = dq[j].first;
				int ey = dq[j].second;
				dist[i][j] = dist[j][i]=solve(x, y, ex, ey);
			}
		}
		dfs(0, 0, 0);
		if (res == MAX)
			cout << -1;
		else
			cout << res;
		cout << "\n";
	}

}





