#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
#define pb push_back
#define pob pop_back
#define ms memset
#define FOR(i,a,b) for(int i = a; i < b; i++)
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef vector<vector<pi>> gra;
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };
int N, M;
int T;
int K;
int res;
int num, num2;
string str;
int dp[10001];
vec v;
int solve(int idx)
{
	if (idx == 0)return 0;
	int& ret = dp[idx];
	if (ret != -1)return ret;
	ret = MAX;
	for (int i = 0; i < N; i++)
	{
		if (idx - v[i] >= 0)
			ret = min(ret, solve(idx - v[i]) + 1);
	}
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> K;
	memset(dp, -1, sizeof(dp));
	for (i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}
	res = solve(K);
	if (res == MAX)
		res = -1;
	cout << res;
}






