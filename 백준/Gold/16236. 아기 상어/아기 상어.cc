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
typedef tuple<int, int, int> tup;
typedef vector<vector<pi>> gra;
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };
int N, M;
int T;
int K;
int res;
int num, num2;
string str;
queue<tup>q;
int m[21][21];
int visited[21][21];
deque<tup>fish;
bool is_inside(int x,int y)
{
	return x >= 0 && x < N&& y >= 0 && y < N;
}
int find_possible(int x, int y,int X,int Y,int cost)
{
	queue<tup>q;
	q.push({ 0,x,y });
	while (!q.empty())
	{
		int cnt, cur_x, cur_y;
		tie(cnt, cur_x, cur_y) = q.front();
		q.pop();
		if (cur_x == X && cur_y == Y)
		{
			return cnt;
		}
		for (int i = 0; i < 4; i++)
		{
			int n_x = cur_x + dx[i];
			int n_y = cur_y + dy[i];
			if (visited[n_x][n_y] || cost < m[n_x][n_y] || !is_inside(n_x, n_y))continue;
			visited[n_x][n_y] = 1;
			q.push({cnt+1,n_x,n_y });
		}
	}
	return 0;
}
int solve()
{
	int cost, x, y;
	tie(cost, x, y) = q.front();
	q.pop();
	int eat_cnt = 0;
	while (1)
	{
		int i;
		int cnt = 0;
		int flag = 0;
		vector<pi>temp;
		int dist = MAX;
		int idx = -1;
		int n_x, n_y;
		for (i = 0; i < fish.size(); i++)
		{
			int f_cost, f_x, f_y;
			tie(f_cost, f_x, f_y) = fish[i];
			if (f_cost >=cost)break;
			memset(visited, 0, sizeof(visited));
			visited[x][y] = 1;
			int next_dist = find_possible(x, y, f_x, f_y, cost);
			if (next_dist)
			{
				if (dist >= next_dist)
				{
					if (dist == next_dist)
					{
						if (n_x >=f_x)
						{
							if (n_x == f_x)
							{
								if (n_y > f_y)
								{
									n_x = f_x;
									n_y = f_y;
									idx = i;
								}
							}
							else
							{
								n_x = f_x;
								n_y = f_y;
								idx = i;
							}
						}
					}
					else if (dist > next_dist)
					{
						n_x = f_x;
						n_y = f_y;
						dist = next_dist;
						idx = i;
					}
				}
			}
		}
		if (idx == -1)
			break;
		else
		{
			x = n_x;
			y = n_y;
			eat_cnt++;
			if (eat_cnt == cost)
			{
				cost++;
				eat_cnt = 0;
			}
			m[n_x][n_y] = 0;
			fish.erase(fish.begin() + idx);
			res += dist;
		}
		if (fish.empty())return res;
	}
	return res;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	for (i = 0; i < N; i++)
	{
		FOR(j, 0, N)
		{
			cin >> m[i][j];
			if (m[i][j])
			{
				if (m[i][j] == 9)
				{
					q.push({ 2, i,j });
					m[i][j] = 0;
				}
				else
					fish.push_back({ m[i][j], i, j });
			}
		}
	}
	sort(fish.begin(), fish.end());
	cout<<solve();
}





