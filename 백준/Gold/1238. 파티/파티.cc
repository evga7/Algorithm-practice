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
int d[1001];
bool is_inside(int x, int y)
{
	if (x >= N || x < 0 || y < 0 || y >= M)return false;
	return true;
}
vector<int> solve(int x)
{
	priority_queue<pi, vector<pi>, greater<pi>>pq;
	pq.push({ 0,x });
	vector<int>dist;
	dist.resize(1001);
	fill(dist.begin(), dist.end(), MAX);
	dist[x] = 0;
	while (!pq.empty())
	{
		int cur = pq.top().second;
		int cost = pq.top().first;
		pq.pop();
		for (auto g : graph[cur])
		{
			int c = g.first+cost;
			int next = g.second;
			if (dist[next] > c)
			{
				dist[next] = c;
				pq.push({ c,next });
			}
		}
	}
	return dist;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M >> X;
	graph.resize(N + 1);
	int x, y, t;
	for (i = 0; i < M; i++)
	{
		cin >> x >> y >> t;
		graph[x].push_back({ t,y });
	}
	for (i = 1; i <= N; i++)
	{
		vector<int>t1, t2;
		t1 = solve(i), t2 = solve(X);
		d[i] = t1[X] + t2[i];
		res = max(d[i], res);
	}
	cout << res;
	
}



