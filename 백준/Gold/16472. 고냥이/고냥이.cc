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
int N, M;
int D;
int T;
int res=1;
int num, num2;
string str;
vec2 v;
int cnt[26];
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> str;
	int left = 0;
	int right = 0;
	int S = str.size();
	int cur = 1;
	cnt[str[0] - 'a']++;
	while (left<S&&right < S)
	{
		right++;
		if (right == S)
			break;
		if (cnt[str[right] - 'a']++ == 0)
		{
			cur++;
		}
		if (cur <= N)
			res = max(res, right - left + 1);
		while (cur > N && left < right)
		{
			if (cnt[str[left] - 'a']-- == 1)
			{
				cur--;
			}
			left++;
		}
	}
	cout << res;
}



