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
int res = INT_MAX;
int N, M, T;
int num;
int t;
int K;
int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };
int R, X;
vec v;
void solve(int back,int idx,int cnt,int sub)
{
	if (idx >= N)
	{
		res = min(cnt, res);
		return;
	}
	if (v[idx]-back == sub)
		solve(v[idx], idx + 1, cnt, sub);
	else if ((v[idx] + 1)-back == sub)
		solve(v[idx]+1, idx + 1, cnt + 1, sub);
	else if ((v[idx] - 1)-back == sub)
		solve(v[idx]-1, idx + 1, cnt + 1, sub);
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}
	solve(v[1]-1, 2, 2, (v[1] - 1) - (v[0]+1));
	solve(v[1]-1, 2, 2, (v[1] - 1) - (v[0]-1));
	solve(v[1]-1, 2, 1, (v[1] - 1) - v[0]);

	solve(v[1]+1, 2, 1, (v[1] + 1) - v[0]);
	solve(v[1]+1, 2, 2, (v[1] + 1) - (v[0] - 1));
	solve(v[1]+1, 2, 2, (v[1] + 1) - (v[0] + 1));

	solve(v[1], 2, 1, v[1] - (v[0] - 1));
	solve(v[1], 2, 0, v[1]  - v[0]);
	solve(v[1], 2, 1, v[1] - (v[0] + 1));

	if (res == INT_MAX)
		res = -1;
	cout << res;
	
}
