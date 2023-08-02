#include <iostream>
#include <vector>
#include <cstring>

using namespace std;
int dp[10001];
int N, M;
int a[10001];
int go(int idx) {
	if (idx == N)return 0;
	int& ret = dp[idx];
	if (ret != -1)
		return ret;
	ret = 987654321;
	for (int i = 0; i < M; i++)
	{
		if (idx + a[i] <= N)
			ret = min(ret, go(idx + a[i])+1);
		for (int j = i + 1; j < M; j++)
		{
			if (idx + a[i] +a[j] <= N)
				ret = min(ret, go(idx + a[i]+a[j])+1);
		}
	}
	return ret;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	cin >> N >> M;
	memset(dp, -1, sizeof(dp));
	for (int i = 0; i < M; i++) {
		cin >> a[i];
	}
	int res=go(0);
	if (res == 987654321)
		res = -1;
	cout << res;

}