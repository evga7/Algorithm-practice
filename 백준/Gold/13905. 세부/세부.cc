#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD  1000000009
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef pair<string, int> psi;
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
int dx[4] = {0,-1,0,1 };
int dy[4] = { -1,0,1,0 };
int L;
vec v;
int res;
int N, M;
int s, e;
gra g;
int visited[100001];
bool solve(int mid)
{
	queue<int>q;
	q.push(e);
	memset(visited, 0, sizeof(visited));
	while (!q.empty())
	{
		int cur = q.front();
		q.pop();
		if (cur == s) return true;
		for (auto cur : g[cur])
		{
			int next = cur.first;
			int cost = cur.second;
			if (visited[next] || cost < mid)continue;
			visited[next] = 1;
			q.push(next);
		}
	}
	return false;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M;
	cin >> s >> e;
	int a, b, c;
	g.resize(N + 1);
	for (int i = 0; i < M; i++)
	{
		cin >> a >> b >> c;
		g[a].push_back({ b,c });
		g[b].push_back({ a,c });
	}
	int left = 0;
	int right = 10000000;
	while (left <= right)
	{
		int mid = (left + right) >> 1;
		if (solve(mid))
		{
			left = mid + 1;
			res = max(res, mid);
		}
		else
			right = mid - 1;
		
	}
	cout<<res;
}
