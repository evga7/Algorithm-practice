#include <bits/stdc++.h>
#define MAX 1000000001
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
int dx[4] = { 0,-1,0,1 };
int dy[4] = {-1,0,1,0 };
int N,M;
int dp[3][1001][31];
int W;
int res = 0;
vector<int>v;
int solve(int pos,int cnt,int w) {
	

	if (cnt == N) {
		return 0;
	}
	int& ret = dp[pos][cnt][w];
	if (ret!=-1)return ret;
	if (pos == v[cnt])
	{
		if (w)
		{
			return ret = max(1 + solve(pos, cnt + 1, w), solve(3 - pos, cnt + 1, w - 1));
		}
		else
			return ret = 1 + solve(pos, cnt + 1, w);
	}
	else
	{
		if (w)
			return ret = max(1 + solve(3 - pos, cnt + 1, w - 1), solve(pos, cnt + 1, w));
		else
			return ret = solve(pos, cnt + 1, w);
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> W;
	int i;
	for (i = 0; i < N; i++)
	{
		int num;
		cin >> num;
		v.push_back(num);
	}
	fill(&dp[0][0][0], &dp[2][1000][30], -1);
	cout<<solve(1, 0, W);
}



