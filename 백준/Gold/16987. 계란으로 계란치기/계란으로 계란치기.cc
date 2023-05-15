#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
#define pb push_back
#define pob pop_back
#define FOR(i,a,b) for(int i = a; i < b; i++)
using namespace std;
typedef long long int ll;
typedef unsigned long long int lll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef vector<vector<pi>> gra;
int dx[4] = { 0, 0,-1,1 };
int dy[4] = { 1,-1,0,0 };
int N, M;
int D;
int T;
int res;
int num, num2;
int sum;
string str;
vec2 v;
void solve(int idx)
{
	int i;
	if (idx == N)
	{
		int cnt2 = 0;
		for (i = 0; i < N; i++)
		{
			if (v[i].first <= 0)
				cnt2++;
		}
		res = max(res, cnt2);
		return;
	}
	if (v[idx].first <= 0)solve(idx + 1);
	else
	{
		bool flag = false;
		for (i = 0; i < N; i++)
		{
			if (i == idx || v[i].first <= 0)continue;
			v[idx].first -= v[i].second;
			v[i].first -= v[idx].second;
			flag = true;
			solve(idx + 1);
			v[i].first += v[idx].second;
			v[idx].first += v[i].second;
		}
		if (!flag)solve(N);
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	for (i = 0; i < N; i++)
	{
		cin >> num >> num2;
		v.push_back({ num,num2 });
	}
	solve(0);
	cout << res;
}







