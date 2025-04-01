#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000009
#define pb push_back
#define pob pop_back
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
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
ll res;
int num, num2;
int T;
int V;
int visited[1001];
vvec g;
void solve(int start)
{
	cout << start << " ";
	visited[start] = 1;
	for (auto next : g[start])
	{
		if (!visited[next])
		{
			visited[next] = 1;
			solve(next);
		}
	}
}
void solve2()
{
	queue<int>q;
	q.push(V);
	memset(visited, 0, sizeof(visited));
	visited[V] = 1;
	while (!q.empty())
	{
		int cur = q.front();
		cout << cur << " ";
		q.pop();
		for (auto next : g[cur])
		{
			if (!visited[next])
			{
				visited[next] = 1;
				q.push(next);
			}
		}

	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i;
	cin >> N >> M >> V;
	g.resize(N + 1);
	for (i = 0; i <M ; i++)
	{
		cin >> num >> num2;
		g[num].push_back(num2);
		g[num2].push_back(num);
	}
	for (i = 1; i <= N; i++)
	{
		sort(g[i].begin(), g[i].end());
	}
	solve(V);
	cout << "\n";
	solve2();
}




