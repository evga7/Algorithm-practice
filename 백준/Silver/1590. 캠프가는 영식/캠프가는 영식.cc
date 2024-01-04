#include <bits/stdc++.h>
#define MAX 1000000001
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, pair<int, int>>pi2;
ll N, T;
ll S, intv, M;
int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };
int res = 0;
vector<ll>v;
int main()
{
	ios::sync_with_stdio(false), cin.tie(NULL);	cout.tie(NULL);
	cin >> N >> T;
	int i, j;
	int num;
	ll res = MAX;
	for (i = 0; i < N; i++)
	{
		cin >> S >> intv >> M;
		v.clear();
		ll r = MAX;
		ll left = 0;
		ll right = M-1;
		while (left <=right)
		{
			ll mid = left + right >> 1;
			ll temp = S + intv * mid;
			if (temp == T)
			{
				r = 0;
				break;
			}
			if (temp > T)
			{
				r = min(r, abs(temp - T));
				right = mid - 1;
			}
			else
			{
				left = mid + 1;
			}
		}
		res = min(res, r);
	}
	if (res == MAX)
		cout << "-1\n";
	else
		cout << res << "\n";
}