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
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int res;
int num;
int K;
vector<vec2>graph;
int dist[20001];
bool is_inside(int x, int y)
{
	if (x >= N || x < 0 || y < 0 || y >= M)return false;
	return true;
}
void solve()
{
	priority_queue<pi,vector<pi>,greater<pi>>pq;
	pq.push({ 0,K });
	dist[K] = 0;
	while (!pq.empty())
	{
		int cur = pq.top().second;
		int cost = pq.top().first;
		pq.pop();
		int i;
		for (auto g : graph[cur])
		{
			int c = cost + g.first;
			int next = g.second;
			if (dist[next] > c)
			{
				dist[next] = c;
				pq.push({ c,next });
			}
		}
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M >> K;
	int a, b, c;
	graph.resize(N + 1);
	for (i = 0; i < M; i++)
	{
		cin >> a >> b >> c;
		graph[a].push_back({ c,b });
	}
	fill(dist, dist + N + 1, MAX);
	solve();
	for (i = 1; i <= N; i++)
	{
		if (dist[i] == MAX)cout << "INF";
		else
			cout << dist[i];
		cout << "\n";
	}
}



