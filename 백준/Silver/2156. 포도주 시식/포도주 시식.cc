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
int res = MAX;
int arr[10003];
int dp[10001][4];
int solve(int n,int cnt)
{
	if (n >=N)
		return 0;
	int& ret = dp[n][cnt];
	if (ret != -1)return ret;
	if (cnt == 1)
	{
		ret = max(solve(n + 3, 0), solve(n + 2, 0));
	}
	else
		ret = max({ ret,solve(n + 1,cnt+1),solve(n + 2,0) });
	ret += arr[n];
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	for (i = 0; i <N; i++)
	{
		cin >> arr[i];
	}
	memset(dp, -1, sizeof(dp));
	cout << max({solve(0, 0),solve(1,0),solve(2,0) });
}


