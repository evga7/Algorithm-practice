#include <stdio.h>
int dp[100001][3];
int main()
{
	int N;
	int i;
	scanf("%d", &N);
	dp[0][0] = { 0 };
	dp[1][0] = dp[1][1] = dp[1][2] = 1;
	for (i = 2; i <= N+1; i++)
	{
		dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901;
		dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901;
		dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901;
	}
	printf("%d", dp[N+1][0] % 9901);
}