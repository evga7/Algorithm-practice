#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
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
int dp[1001];
int arr[1001];
int solve(int idx)
{
	if (idx == N)return 0;
	int& ret = dp[idx];
	if (ret != -1)return ret;
	ret = arr[idx];
	int i;
	for (i = idx+1; i < N; i++)
	{
		if (arr[idx]<arr[i])
		ret = max(ret, solve(i) + arr[idx]);
	}
	return ret;

}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	for (i = 0; i < N; i++)
		cin >> arr[i];
	memset(dp, -1, sizeof(dp));
	for (i = 0; i < N; i++)
		res = max(res, solve(i));
	cout << res;
}



