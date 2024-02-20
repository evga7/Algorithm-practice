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
int N, M, T;
ll dp[100001][4];
int arr[100001];
vec v;
ll solve(int idx,int cnt)
{
	if (idx == 0)return 1;
	ll& ret = dp[idx][cnt];
	if (ret != -1)return ret;
	ret = 0;
	for (int i = 1; i <= 3; i++)
	{
		if (idx-i>=0 && cnt!=i)
			ret += solve(idx - i,i)% (1000000009);
	}
	return ret% 1000000009;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> T;
	memset(dp, -1, sizeof(dp));
	while (T)
	{
		T -= 1;
		cin >> N;
		cout << solve(N,0) % (1000000009) << "\n";

	}
	
}
