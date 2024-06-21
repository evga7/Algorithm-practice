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
string str2;
int dp[1001][1001];
int solve(int idx, int idx2)
{
	if (idx == N || idx2 == M)return 0;
	int& ret = dp[idx][idx2];
	if (ret != -1)return ret;
	ret = 0;
	if (str[idx] == str2[idx2])
		ret = max(ret, solve(idx + 1, idx2 + 1) + 1);
	else
		ret = max({ ret,solve(idx + 1,idx2),solve(idx,idx2 + 1) });
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	memset(dp, -1, sizeof(dp));
	cin >> str >> str2;
	N = str.size();
	M = str2.size();
	cout << solve(0, 0);
}






