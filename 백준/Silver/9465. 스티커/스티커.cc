

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
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int res;
int T;
int num,num2;
int dp[3][100001];
int arr[2][100001];
int solve(int n,int r)
{
	if (r >=N)return 0;
	int& ret = dp[n][r];
	if (ret != -1)return ret;
	if (n == 0)
		ret = max(solve(n + 1, r + 1),solve(n+1,r + 2) ) + arr[n][r];
	else if (n == 1)
		ret = max(solve(n - 1, r + 1),solve(n -1,r + 2)) + arr[n][r];
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> T;

	while (T--)
	{
		cin >> N;
		memset(dp, -1, sizeof(dp));
		for (i = 0; i < N; i++)
		{
			cin >> arr[0][i];
		}
		for (i = 0; i < N; i++)
		{
			cin >> arr[1][i];
		}
		cout << max(solve(0, 0),solve(1,0)) << "\n";
	}
}


