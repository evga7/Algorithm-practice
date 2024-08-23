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
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
int N, M, K, T;
string str;
int re;
vector<pii>v;
int dp[100][10001];
bool is_inside(int x, int y)
{
	return y <=x;
}
int go(int idx, int t)
{
	if (idx == N)
		return 0;
	int& ret = dp[idx][t];
	if (ret != -1)
		return ret;
	ret = 0;
	if (t - v[idx].first >= 0)
		ret = max(ret, go(idx + 1, t - v[idx].first) + v[idx].second);
	ret = max(ret, go(idx + 1, t));
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N>>M;
	memset(dp, -1, sizeof(dp));
	for (int i = 0; i < N; i++)
	{
		int a, b;
		cin >> a >> b;
		v.push_back(make_pair(a, b));
	}
	cout << go(0, M);
}