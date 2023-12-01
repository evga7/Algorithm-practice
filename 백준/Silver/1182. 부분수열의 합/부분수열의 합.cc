#include <iostream>
#include <math.h>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
int arr[21];
int chk[21];
int n,s;
int cnt = 0;
void dfs(int start, int sum)
{
	sum += arr[start];
	if (start == n)
		return;
	if (sum == s)
	{
		cnt++;
	}

	dfs(start + 1, sum -arr[start]);
	dfs(start + 1, sum);
}
int main() {
	int i;
	scanf("%d %d", &n, &s);
	for (i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	dfs(0,0);
	printf("%d", cnt);
}