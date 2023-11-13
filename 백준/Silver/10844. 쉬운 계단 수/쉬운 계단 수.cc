#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <sstream>
#include <stack>
#include <set>
#include <map>
#define MAX 987654321
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
int N;
ll dp[101][10];
int arr[10001];
int main()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int i;
	cin >> N;
	for (i = 1; i <= 9; i++)
		dp[1][i] = 1;
	for (i = 2; i <=N; i++)
	{
		dp[i][0] = dp[i - 1][1];
		dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]);
		dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % 1000000000;
		dp[i][3] = (dp[i - 1][2] + dp[i - 1][4]) % 1000000000;
		dp[i][4] = (dp[i - 1][3] + dp[i - 1][5]) % 1000000000;
		dp[i][5] = (dp[i - 1][4] + dp[i - 1][6]) % 1000000000;
		dp[i][6] = (dp[i - 1][5] + dp[i - 1][7]) % 1000000000;
		dp[i][7] = (dp[i - 1][6] + dp[i - 1][8]) % 1000000000;
		dp[i][8] = (dp[i - 1][7] + dp[i - 1][9]) % 1000000000;
		dp[i][9] = (dp[i - 1][8]);

	}
	ll res = 0;
	for (i = 0; i < 10; i++)
		res += dp[N][i]% 1000000000;
	cout << res % 1000000000;
}