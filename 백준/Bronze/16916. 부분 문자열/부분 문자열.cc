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
int dx[4] = { 0, 0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int N, M, T;
int S;
int K;
int res;
int num, num2;
bool flag[26];
string s, p;
vec getPi(const string &p)
{
	int m = p.size(), j = 0;
	vec pi(m, 0);
	for (int i = 1; i < m; i++)
	{
		while (j > 0 && p[i] != p[j])
		{
			j = pi[j - 1];
		}
		if (p[i] == p[j])
			pi[i] = ++j;
	}
	return pi;
}
int kmp(const string& s, const string& p)
{
	auto pi = getPi(p);
	int n = s.size(), m = p.size(), j = 0;
	for (int i = 0; i < n; i++)
	{
		while (j > 0 && s[i] != p[j])
		{
			j = pi[j - 1];
		}
		if (s[i] == p[j])
		{
			if (j == m - 1)
			{
				return 1;
				j = pi[j];
			}
			else
				j++;
		}
	}
	return 0;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> s >> p;
	cout<<kmp(s, p);
	
}



