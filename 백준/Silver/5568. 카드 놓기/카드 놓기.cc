#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
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
int N, M, T;
ll res;
int L;
int num;
int V, E, K;
vec v;
vec v2;
bool c[11];
set<string>s;
void solve(int idx,int cnt)
{
	if (cnt == M)
	{
		string str = "";
		for (auto cur : v2)
		{
			str = str + to_string(v[cur]);
		}
		s.insert(str);
		return;
	}
	for (int i = 0; i < N; i++)
	{
		if (!c[i])
		{
			c[i] = 1;
			v2.push_back(i);
			solve(i + 1, cnt + 1);
			v2.pop_back();
			c[i] = 0;
		}

	}
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M;
	int i;
	for (i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}
	solve(0,0);
	cout << s.size();
}





