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
int in[501];
vpi v;
int cost[501];
int r[501];
void solve()
{
	queue<int>q;
	int i;
	for (i = 1; i <= N; i++)
	{
		if (!in[i])
			q.push(i), r[i] = cost[i];
	}
	while (!q.empty())
	{
		int cur = q.front();
		q.pop();
		for (auto g : v[cur])
		{
			if (--in[g] == 0)
			{
				q.push(g);
			}
			r[g] = max(r[g], cost[g] + r[cur]);
		}
	}
	for (i = 1; i <= N; i++)
	{
		cout << r[i] << "\n";
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	v.resize(N + 1);
	for (i = 1; i <=N; i++)
	{
		cin >> num;
		cost[i] = num;
		while (1)
		{
			cin >> num;
			if (num == -1)break;
			else
				v[num].push_back(i), in[i]++;
		}
	}
	solve();

}



