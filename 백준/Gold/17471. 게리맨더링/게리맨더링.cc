#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000000
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
int res = MAX;
int num, num2;
int T;
int K;
int flag;
int cost[11];
int visited[11];
int c[11];
vector<vec>v;
vec v2;
bool chk(int cnt2,int op)
{
	int i, j;
	queue<int>q;
	int cnt = 1;
	int visited2[11] = { 0, };
	memset(c, 0, sizeof(c));
	for (i = 1; i <= N; i++)
	{
		c[i] = visited[i];
	}
	for (i = 1; i <= N; i++)
	{
		if (op)
		{
			if (c[i])
			{
				visited2[i] = 1;
				q.push(i);
				break;
			}
		}
		else
		{
			if (!c[i])
			{
				visited2[i] = 1;
				q.push(i);
				break;
			}
		}
	}
	while (!q.empty())
	{
		int cur = q.front();
		q.pop();
		for (auto next : v[cur])
		{
			if (!visited2[next])
			{
				if (op)
				{
					if (c[next])
					{
						visited2[next] = 1;
						q.push(next);
						cnt++;
					}
				}
				else
				{
					if (!c[next])
					{
						visited2[next] = 1;
						q.push(next);
						cnt++;
					}
				}
			}
		}

	}
	if (cnt2 == cnt)
		return true;
	return false;
}
void solve(int cnt, int n, int idx)
{
	int i;
	if (cnt == n)
	{
		int flag1, flag2;
		flag1 = chk(n,1);
		flag2 = chk(N-n,0);
		int temp1, temp2;
		temp1 = temp2 = 0;
		if (flag1 && flag2)
		{
			for (i = 1; i <= N; i++)
			{
				if (visited[i])
					temp1 += cost[i];
				else
					temp2 += cost[i];
			}
			res = min(res, abs(temp2 - temp1));
		}
		return;
	}
	for (i = idx; i <= N; i++)
	{
		if (!visited[i])
		{
			visited[i] = 1;
			solve(cnt + 1, n, i + 1);
			visited[i] = 0;
		}
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
	for (i = 1; i <= N; i++)
	{
		cin >> cost[i];
	}
	for (i = 1; i <= N; i++)
	{
		cin >> M;
		for (j = 0; j < M; j++)
		{
			cin >> num;
			v[i].push_back(num);
		}
	}
	for (i = 1; i < N; i++)
	{
		for (j = 1; j <=N; j++)
		{
			visited[j] = 1;
			solve(1, i, j);
			visited[j] = 0;
		}
	}
	if (res == MAX)res = -1;
	cout << res;
}




