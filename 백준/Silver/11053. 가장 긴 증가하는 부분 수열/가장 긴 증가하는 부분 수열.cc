#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int arr[1001];
int dp[1001];
int main()
{
	int N;
	scanf("%d", &N);
	int i, j;
	int res=-1;
	int min;
	for (i = 0; i < N; i++)
		scanf("%d", &arr[i]);
	for (i = 0; i < N; i++)
	{
		min = 0;
		for (j = 0; j <i; j++)
		{
			if (arr[i] > arr[j]&&dp[j]>min)
			{
				min = dp[j];
			}
		}
		dp[i] = min + 1;
		res = max(dp[i], res);
	}
	printf("%d", res);
}
