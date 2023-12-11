#include <bits/stdc++.h>
#define MAX 2147483647
#define MIN -2147483648
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
int num;
vec2 v;
int dp[101][10001];
int solve(int cnt, int sum)
{
	if (cnt >= N)return 0;
	int& ret = dp[cnt][sum];
	if (ret != -1)return ret;
	ret = solve(cnt + 1, sum);
	if (v[cnt].second <= sum)
		ret = max(ret, v[cnt].first + solve(cnt + 1, sum - v[cnt].second));
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	v.resize(N);
	for (i = 0; i < N; i++)
		cin >> num, v[i].first = num;
	for (i = 0; i < N; i++)
		cin >> num, v[i].second = num;
	memset(dp, -1, sizeof(dp));
	for (i = 0; i <= 10000; i++)
	{
		if (M <= solve(0, i))
		{
			cout << i;
			return 0;
		}
	}
}



