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
int K;
int res;
int L;
int num;
string str;
string res_s;
int cnt[26];
vector<string>v;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	for (i = 0; i < N; i++)
	{
		cin >> str;
		v.push_back(str);
	}
	for (i=0;i<M;i++)
	{
		int idx = 27;
		int m = 0;
		memset(cnt, 0, sizeof(cnt));
		for (j=0;j<N;j++)
		{
			int c = v[j][i] - 'A';
			cnt[c]++;
			if (m <= cnt[c])
			{
				if (m == cnt[c])
				{
					if (idx > c)
					{
						idx = c;
					}
					continue;
				}
				m = cnt[c];
				idx = c;
			}
		}
		res_s.push_back('A' + idx);
		res += N - m;
	}
	cout << res_s << "\n" << res;
}




