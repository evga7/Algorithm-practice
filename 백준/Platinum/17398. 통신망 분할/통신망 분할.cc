#include <bits/stdc++.h>
#define MAX 1000000001
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, pair<int, int>>pi2;
int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };
ll res = 0;
int N,M,Q;
int parent[100001];
int visited[100001];
ll cost[100001];
vector<int>v;
vector<pi>graph;
int find(int x)
{
	if (x == parent[x])return x;
	return parent[x] = find(parent[x]);
}
void uni(int x, int y,int chk)
{
	x = find(x);
	y = find(y);
	if (x != y)
	{
		if (chk)
			res += cost[x] * cost[y];
		cost[y] += cost[x];
		parent[x] = y;
		
	}
}
int main()
{
	ios::sync_with_stdio(false), cin.tie(NULL);	cout.tie(NULL);
	int i;
	cin >> N >> M>>Q;	
	int a, b;
	for (i=0;i<M;i++)
	{
		cin >> a >> b;
		graph.push_back({ a,b });
	}
	for (i = 0; i < Q; i++)
	{
		cin >> a;
		visited[a-1] = 1;
		v.push_back(a-1);
	}
	for (i = 1; i <= N; i++)
	{
		cost[i] = 1;
		parent[i] = i;
	}

	for (i = 0; i <M; i++)
	{
		if (visited[i])continue;
		int x = graph[i].first;
		int y = graph[i].second;
		uni(x, y,0);
	}
	for (i = Q- 1; i >= 0; i--)
	{
		int idx = v[i];
		int x = graph[idx].first;
		int y = graph[idx].second;
		uni(x, y,1);
	}

	cout << res<<"\n";
}