#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 99999999999999999
#define MIN -987654321
#define MOD 1000000007
#define pb push_back
#define pob pop_back
#define FOR(i,a,b) for(int i = a; i < b; i++)
using namespace std;
typedef unsigned long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef vector<vector<pi>> gra;
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,1,0,-1 };
int N, M;
int L;
int T;

int res;
int num, num2;
int sum;
string str;
ll dp[101][101];
int s[11] = {6,2,5,5,4,5,6,3,7,6 };
ll solve(int idx, int cnt,ll sum)
{
	if (cnt < 0)return MAX;
	if (cnt ==0)return sum;
	ll& ret = dp[idx][cnt];
	if (ret != -1)return ret;
	ret = MAX;
	if (sum&&cnt - s[0] >= 0)
		ret=min(ret,solve(idx + 1, cnt - s[0],sum*10)) ;
	for (int i = 1; i <= 9; i++)
	{
		if (cnt - s[i] >= 0)
			ret = min(ret, solve(idx + 1, cnt - s[i],sum* 10 + i));
	}
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> T;
	while (T--)
	{
		cin >> N;
		memset(dp, -1, sizeof(dp));
		cout << solve(0, N,0) << " ";
		while (N>=2)
		{
			if (N&1)
			{
				N -= 3;
				cout << 7;
			}
			else
			{
				cout << 1;
				N -= 2;
			}
		}
		cout << "\n";
	}
}







