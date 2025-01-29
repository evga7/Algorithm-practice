#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
int dx[4] = { 0, 0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int N, M, T;
int Q;
int S, G, H;
int res;
int num, num2;
vec v;
gra g;
int dist_S[2001];
vec dest;
void solve(int start, int dist[2001])
{
	priority_queue<pii>pq;
	pq.push({ 0,start });
	dist[start] = 0;
	while (!pq.empty())
	{
		int cur = pq.top().second;
		int cost = -pq.top().first;
		pq.pop();
		for (auto n : g[cur])
		{
			int next = n.second;
			int n_cost = n.first + cost;
			if (dist[next] > n_cost)
			{
				dist[next] = n_cost;
				pq.push({ -n_cost,next });
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
	cin >> Q;
	int a, b, c;
	while (Q--)
	{
		cin >> N >> M >> T;
		cin >> S >> G >> H;
		g.clear();
		g.resize(N + 1);
		fill(dist_S, dist_S + N + 1, MAX);
		for (i = 0; i < M; i++)
		{
			cin >> a >> b >> c;
			c *= 2;
			if ((a == G && b == H) || (a == H && b == G))
				c--;
			g[a].push_back({ c,b });
			g[b].push_back({ c,a });
		}
		dest.clear();
		for (i = 0; i < T; i++)
		{
			cin >> num;
			dest.push_back(num);
		}
		solve(S, dist_S);
		sort(dest.begin(), dest.end());
		for (i = 0; i < dest.size(); i++)
		{
			int des = dest[i];
			if (dist_S[des] & 1&&dist_S[des]!=MAX)
				cout << des << " ";
		}
		cout << "\n";
	}
}



