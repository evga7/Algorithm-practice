#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD  1000000009
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef pair<string, int> psi;
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<ll> vecll;
typedef vector<pii> vpi;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
int L;
int res;
int N, M, T;
int num;
//왼 위 오 아래
int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };
int t[1500001];
int p[1500001];
int dp[1500001];
int solve(int idx)
{
	if (idx > N)return 0;
	int& ret = dp[idx];
	if (ret != -1)return ret;
	ret = 0;
	if (idx + t[idx] <= N)
		ret = solve(idx + t[idx])+ p[idx];
	ret = max(ret, solve(idx + 1));
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	for (int i=0;i<N;i++)
		cin >> t[i] >> p[i];
	memset(dp, -1, sizeof(dp));
	cout<<solve(0);
}
