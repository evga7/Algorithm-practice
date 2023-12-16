#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000009
#define pb push_back
#define pob pop_back
#define ms memset
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
int T;
int H;
int res;
int num, num2;
string str;
vvec g;
vec v;
int visited[100001];
int cnt;
void solve(int start)
{
	visited[start] = 1;
	for (auto a:g[start])
	{
		if (!visited[a])
		{
			cnt++;
			solve(a);
		}
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	g.resize(N + 1);
	for (i = 0; i < M; i++)
	{
		cin >> num >> num2;
		g[num2].push_back(num);
	}
	for (i = 1; i <= N; i++)
	{
		cnt = 0;
		ms(visited, 0, sizeof(visited));
		solve(i);
		if (res == cnt)
		{
			v.push_back(i);
		}
		else if (res < cnt)
		{
			res = cnt;
			v.clear();
			v.push_back(i);
		}
	}
	for (auto a : v)
		cout << a << " ";
}




