#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;
int chk[20000001];

int main(void)
{
	int N,M;
	int i;
	int num;
	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%d", &num);
		if (num <=0)
			chk[abs(num)]++;
		else
			chk[num + 10000000]++;
	}
	scanf("%d", &M);
	for (i = 0; i < M; i++)
	{
		scanf("%d", &num);
		if (num <=0)
		{
			if (chk[abs(num)])
				printf("1 ");
			else
				printf("0 ");
		}
		else
		{
			if (chk[num + 10000000])
				printf("1 ");
			else
				printf("0 ");
		}
	}

}