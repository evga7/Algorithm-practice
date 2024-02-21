#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000009
#define pb push_back
#define pob pop_back
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
int S;
vec v;
vec v2;
int dp[100001][2];
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	for (i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}
    res=v[0];
	dp[0][0] = v[0];
	dp[0][1] = 0;
	for (i = 1; i < N; i++)
	{
		dp[i][0] = max(dp[i - 1][0] + v[i], v[i]);
		dp[i][1] = max(dp[i - 1][1] + v[i], dp[i - 1][0]);
		res = max({ res,dp[i][0], dp[i][1] });
	}
	cout << res;
}




