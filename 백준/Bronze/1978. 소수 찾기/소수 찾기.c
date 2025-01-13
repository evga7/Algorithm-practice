#include <stdio.h>
int prime[1001];
int arr[101];
int main(){
	int N;
	int i,j;
	int cnt = 0;
	memset(prime, 1, sizeof(prime));
	prime[0]=prime[1] = 0;
	for (i = 2; i <=32; i++)
	{
		for (j = i * i; j<= 1001; j+=i)
		{
			if (prime[j])
			{
				prime[j] = 0;
			}
		}
	}
	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%d", &arr[i]);
		if (prime[arr[i]])
			cnt++;
	}
	printf("%d", cnt);
}