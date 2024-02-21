#include <bits/stdc++.h>
using namespace std;
int dy[2]={0,1};
int dp[501][501];
int t[501][501];
int N;
int solve(int x,int y){
    if (x==N-1){
        return t[x][y];
    }
    int&ret=dp[x][y];
    if (ret!=-1)return ret;
    return ret=max(solve(x+1,y),solve(x+1,y+1))+t[x][y];
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cin >> t[i][j];
        }
    }
    memset(dp, -1, sizeof(dp));
    cout << solve(0, 0);
}