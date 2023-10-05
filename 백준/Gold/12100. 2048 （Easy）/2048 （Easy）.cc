#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
#define pb push_back
#define pob pop_back
#define FOR(i,a,b) for(int i = a; i < b; i++)
using namespace std;
typedef long long int ll;
typedef unsigned long long int lll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef vector<vector<pi>> gra;
int dx[4] = { 0, 0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int N, M;
int D;
int T;
int res;
int num, num2;
string str;
vec v;
struct board {
	int m[21][21];
	int i, j;
	void up()
	{
		int temp[21][21];
		memset(temp, 0, sizeof(temp));
		for (i = 0; i < N; i++)
		{
			int flag = 0;
			int target = -1;
			for (j = 0; j < N; j++)
			{
				if (!m[j][i])continue;
				if (flag && temp[target][i] == m[j][i])
				{
					temp[target][i] *= 2;
					flag = 0;
				}
				else
				{
					temp[++target][i] = m[j][i];
					flag = 1;
				}
			}
		}

		for (i = 0; i < N; i++)
		{
			for (j = 0; j < N; j++)
			{
				m[i][j] = temp[i][j];
			}
		}
	}
	void rotate()
	{
		int temp[21][21];
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < N; j++)
			{
				temp[j][i] = m[N - 1 - i][j];
			}
		}
		for (i = 0; i < N; i++)
		{
			for (j = 0; j < N; j++)
			{
				m[i][j] = temp[i][j];
			}
		}
	}
	int max_score()
	{
		int s = 0;
		for (i = 0; i < N; i++)
			for (j = 0; j < N; j++)
				s = max(s, m[i][j]);
		return s;
	}
};
void solve(int cnt, board cur)
{
	if (cnt == 5)
	{
		res = max(res, cur.max_score());
		return;
	}
	for (int i = 0; i < 4; i++)
	{
		board next = cur;
		next.up();
		solve(cnt + 1, next);
		cur.rotate();
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	board cur;
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < N; j++)
		{
			cin >> cur.m[i][j];
		}
	}
	solve(0, cur);
	cout << res;
}



