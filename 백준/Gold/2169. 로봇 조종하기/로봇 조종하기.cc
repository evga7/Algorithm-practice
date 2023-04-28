#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 99999999999999999
#define MIN -987654321
#define MOD 1000000007
#define pb push_back
#define pob pop_back
#define FOR(i,a,b) for(int i = a; i < b; i++)
using namespace std;
typedef unsigned long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef vector<vector<pi>> gra;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int N, M;
int L;
int T;
int res;
int num, num2;
int sum;
string str;
int dp[1001][1001][3];
int a[1001][1001];
int solve(int x, int y, int op) {
	if (x == N - 1 && y == M - 1)
		return a[x][y];
	int& ret = dp[x][y][op];
	if (ret != -1)return ret;
	ret = -987654321;
	for (int i = 0; i < 3; i++)
	{
		if (op == 0 && i == 1)continue;
		if (op == 1 && i == 0)continue;
		int n_x = x + dx[i];
		int n_y = y + dy[i];
		if (0 <= n_x && n_x < N && 0 <= n_y && n_y < M) {
			ret = max(ret, solve(n_x, n_y, i) + a[x][y]);
		}
	}
	return ret;

}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> a[i][j];
		}
	}
	memset(dp, -1, sizeof(dp));
	cout << solve (0, 0, 2);
}

