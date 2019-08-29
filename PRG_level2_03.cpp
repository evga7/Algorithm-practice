#include <iostream>
#include <vector>
using namespace std;
int dp[100001][4];
int solution(vector<vector<int> > land)
{
	int answer = 0;
	int i, j;
	int N = land.size();
	for (i = 0; i < N; i++)
	{
		dp[i][0] = land[i][0] + max(max(dp[i - 1][1], dp[i - 1][2]), dp[i - 1][3]);
		dp[i][1] = land[i][1] + max(max(dp[i - 1][0], dp[i - 1][2]), dp[i - 1][3]);
		dp[i][2] = land[i][2] + max(max(dp[i - 1][0], dp[i - 1][1]), dp[i - 1][3]);
		dp[i][3] = land[i][3] + max(max(dp[i - 1][0], dp[i - 1][1]), dp[i - 1][2]);
	}
	answer = max(max(max(dp[N - 1][0], dp[N - 1][1]), dp[N - 1][2]), dp[N - 1][3]);
	return answer;
}