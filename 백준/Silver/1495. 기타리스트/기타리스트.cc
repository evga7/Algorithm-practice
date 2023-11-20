#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000009
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
int S;
int T;
int K;
int res;
int num, num2;
string str;
int dp[101][100001];
int volumn[101];
int solve(int idx,int v)
{
	int& ret = dp[idx][v];
	if (v<0 || v>M)return MIN;
	if (idx == N)return v;
	if (ret != -1)return ret;
	ret = max(solve(idx + 1, v + volumn[idx]), solve(idx + 1, v - volumn[idx]));
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> S >> M;
	memset(dp, -1, sizeof(dp));
	for (i = 0; i < N; i++)
	{
		cin >> volumn[i];
	}
	res=solve(0,S);
	if (res == MIN)
		res = -1;
	cout << res;
}






