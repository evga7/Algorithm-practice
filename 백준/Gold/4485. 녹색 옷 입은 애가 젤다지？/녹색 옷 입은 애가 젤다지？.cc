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
int X;
gra graph;
int m[126][126];
int dist[126][126];
bool is_inside(int x, int y)
{
	if (x >= N || x < 0 || y < 0 || y >= N)return false;
	return true;
}
void solve(int idx)
{
	priority_queue<pi2, vector<pi2>, greater<pi2>>pq;
	pq.push({ m[0][0],{0, 0} });
	fill(&dist[0][0], &dist[N][N], MAX);
	dist[0][0] = 0;
	while (!pq.empty())
	{
		const auto tmp = pq.top();
		int cost = tmp.first;
		int cur_x = tmp.second.first;
		int cur_y = tmp.second.second;
		if (cur_x == N - 1 && cur_y == N - 1)
		{
			printf("Problem %d: %d\n", idx, dist[N - 1][N - 1]);
			return;
		}
		pq.pop();
		int i;
		for (i = 0; i < 4; i++)
		{
			int n_x = cur_x + dx[i];
			int n_y = cur_y + dy[i];
			int c = m[n_x][n_y] + cost;
			if (!is_inside(n_x, n_y) || c >=dist[n_x][n_y])continue;
			dist[n_x][n_y] = c;
			pq.push({ c,{n_x,n_y} });
		}
	}
	
}
int main()
{
	//ios::sync_with_stdio(false);
	//cin.tie(0);
	//cout.tie(0);
	int i, j;
	int cnt = 1;
	while (1)
	{
		cin >> N;
		if (N == 0)break;
		for (i = 0; i < N; i++)
			for (j = 0; j < N; j++)
				scanf("%d", &m[i][j]);
		solve(cnt++);
	}

}



