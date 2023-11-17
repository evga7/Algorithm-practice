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
string str;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	for (i = 0; i < N; i++)
	{
		cin >> str;
		memset(flag, 0, sizeof(flag));
		for (j=0;j<str.size();j++)
		{
			if (!flag[str[j] - 'a'])
			{
				flag[str[j] - 'a'] = 1;
			}
			else
			{
				if (j > 0 && str[j] != str[j - 1])break;
			}
		}
		if (j == str.size())res++;
	}
	cout << res;
}



