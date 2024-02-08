#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
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
//int dx[4] = { 0,1,0,-1 };
//int dy[4] = { 1,0,-1,0 };
int dx[4] = { 0,0,1,1 };
int dy[4] = { 0,1,0,1 };
int N, M;
int res;
int num;
int r, c;
int arr[2200][2200];
void solve(int size, int x, int y)
{
	if (x == r && y == c)
	{
		cout << res;
		return;
	}
	if (r < size + x && x <= r && c < size + y && y <= c)
	{
		int h = size / 2;
		solve(h, x, y);
		solve(h, x, y + h);
		solve(h, x + h, y);
		solve(h, x + h, y + h);
	}
	else
		res += size * size;
	return;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N>>r>>c;
	solve(1<<N, 0, 0);
}

