#include <stdio.h>
int arr[1001];
int dp[1001];
int main()
{
	int i,j;
	int N;
	scanf("%d", &N);
	int max=0;
	for (i = 0; i < N; i++)
	{
		scanf("%d", &arr[i]);
		dp[i] = arr[i];
		for (j = 0; j < i; j++)
		{
			if (arr[j] < arr[i] && dp[i]<dp[j]+arr[i])
			{
				dp[i] = dp[j] + arr[i];
			}
		}
		if (max < dp[i])
			max = dp[i];
	}
	printf("%d", max);
}

