#include <bits/stdc++.h>
#include<regex>
#define MAX 2147483647
#define MIN -2147483648
#define MOD 1000000000
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vpi;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef queue<pii> que;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int T;
int N, M;
int num;
int cnt;
int res;
vec v;
char arr[51][51];
bool visited[51][51][64];
bool is_inside(int x, int y)
{
	return x >= 0 && x < N&& y >= 0 && y < M;
}
typedef struct info {
	int x, y, cnt, key;
}info;
int sx, sy;
void solve()
{
	int i, j;
	queue<info>q;
	q.push({ sx,sy,0,0 });
	visited[sx][sy][0] = 1;
	while (!q.empty())
	{
		int x = q.front().x;
		int y = q.front().y;
		int cnt = q.front().cnt;
		int key = q.front().key;
		q.pop();
		if (arr[x][y] == '1')
		{
			cout << cnt;
			return;
		}
		for (int i = 0; i < 4; i++)
		{
			int n_x = x + dx[i];
			int n_y = y + dy[i];
			if (!is_inside(n_x, n_y) ||arr[n_x][n_y]=='#'||visited[n_x][n_y][key])continue;
			if (arr[n_x][n_y] >= 'a' && arr[n_x][n_y] <= 'f')
			{
				int n_key = key | (1 << (arr[n_x][n_y] - 'a'));
				if (visited[n_x][n_y][n_key])continue;
				q.push({ n_x,n_y,cnt + 1,n_key });
				visited[n_x][n_y][n_key] = 1;
			}
			else if (arr[n_x][n_y] >= 'A' && arr[n_x][n_y] <= 'F')
			{
				int n_key = key & (1 << (arr[n_x][n_y] - 'A'));
				if (n_key == 0)continue;
				q.push({ n_x,n_y,cnt + 1,key });
				visited[n_x][n_y][key] = 1;
			}
			else
			{
				q.push({ n_x,n_y,cnt + 1,key });
				visited[n_x][n_y][key] = 1;
			}
		}
	}
	cout << "-1";
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N>>M;
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < M; j++)
		{
			cin >> arr[i][j];
			if (arr[i][j] == '0')
			{
				sx = i;
				sy = j;
			}
		}
	}
	solve();

}
