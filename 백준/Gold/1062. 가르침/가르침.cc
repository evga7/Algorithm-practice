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
int T;
int K;
int res;
int num, num2;
string str;
vector<string>v;
bool alpha[26];
void solve(int idx,int cnt)
{
	if (cnt == M)
	{
		int i, j;
		int cnt2 = 0;
		for (i = 0; i < N; i++)
		{
			int flag = 0;
			for (j = 0; j < v[i].size(); j++)
			{
				if (!alpha[v[i][j] - 'a'])
				{
					flag = 1;
					break;
				}
			}
			if (!flag)
				cnt2++;
		}
		res = max(res, cnt2);
		return;
	}
	for (int i = idx; i < 26; i++)
	{
		if (!alpha[i])
		{
			alpha[i] = 1;
			solve(i+1,cnt + 1);
			alpha[i] = 0;
		}
	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	alpha['a' - 'a'] = 1;
	alpha['n' - 'a'] = 1;
	alpha['t' - 'a'] = 1;
	alpha['i' - 'a'] = 1;
	alpha['c' - 'a'] = 1;
	M -= 5;
	for (i = 0; i < N; i++)
	{
		cin >> str;
		v.pb(str);
	}
	solve(0, 0);
	cout << res;
}





