
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
int res;
int num, num2;
int T;
int K;
int arr[501][501];
int dp[100001][3];

int solve(int n,int m)
{
	if (n == N)return 1;
	int& ret = dp[n][m];
	if (ret != -1)return ret;
	ret = 0;
	ret = solve(n + 1, 0);
	if (m != 1)
		ret += solve(n + 1, 1)%9901;
	if (m != 2)
		ret += solve(n + 1, 2) % 9901;
	return ret % 9901;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	memset(dp, -1, sizeof(dp));
	cout << solve(0, 0) % 9901;
}



