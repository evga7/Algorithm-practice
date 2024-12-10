#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#include <sstream>
#include <stack>
#include <set>
#include <map>
#define MAX 987654321
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
int N,M;
int i, j;
int arr[1001][1001];
int dp[1001][1001];
int solve(int x, int y)
{
	int& ret = dp[x][y];
	if (ret!=-1)
		return ret;
	if (x == N - 1 && y == M - 1)
		return arr[x][y];
	int a, b, c;
	a = b = c = 0;
	if (x + 1 < N)
		a += arr[x][y]+solve(x + 1, y);
	if (x,y+1<M)
		b += arr[x][y] + solve(x , y+1);
	if (x+1<N&&y+1<M)
		c += arr[x][y] + solve(x + 1, y+1);
	ret = max({ a,b,c });
	return ret;
}
int main()
{
	cin >> N >> M;
	for (i = 0; i < N; i++)
		for (j = 0; j < M; j++)
			cin >> arr[i][j];
	memset(dp, -1, sizeof(dp));
	cout << solve(0, 0);
}