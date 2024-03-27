
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
int dp[501][501];
int arr[501];
int s[501];
vec v;
int solve(int start, int end)
{
	if (start >= end)return 0;
	int& ret = dp[start][end];
	if (ret != -1)return ret;
	ret = MAX;
	for (int i = start; i <=end; i++)
	{
		ret = min(ret, solve(start,i)+solve(i+1,end)+s[end]-s[start-1]);
	}
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
		memset(s, 0, sizeof(arr));
		for (i = 1; i <=N; i++)
		{
			cin >> arr[i];
			s[i] += s[i - 1] + arr[i];
		}
		cout << solve(1, N)<<"\n";
	}
}



