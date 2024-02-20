#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000000
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vpi;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef vector<vector<pi>> gra;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int res;
int num, num2;
int T;
int S;
vec v;
vec v2;
int dp[1001];
int solve(int idx)
{
	if (idx == N)return 1;
	int& ret = dp[idx];
	if (ret != -1)return ret;
	ret = 1;
	int i;
	for (i = idx; i < N; i++)
	{
		if (v[idx] < v[i])
		{
			ret=max(ret,solve(i) + 1);
		}
	}
	return ret;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i,j;
	cin >> N;
	for (i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}
	memset(dp, -1, sizeof(dp));
	for (i = 0; i < N; i++)
	{
		res=max(res,solve(i));
	}
	int temp = res;
	for (i = 0; i < N; i++)
	{
		if (dp[i] == temp)
		{
			if (!v2.empty())
			{
				if (v2.back() < v[i])
				{
					v2.push_back(v[i]);
				}
			}
			else
			{
				v2.push_back(v[i]);
			}
			temp--;
		}
	}
	cout << res << "\n";
	for (auto a : v2)
		cout << a << " ";
}




