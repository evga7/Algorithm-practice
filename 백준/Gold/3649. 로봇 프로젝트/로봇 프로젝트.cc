#include <bits/stdc++.h>
#define MAX 1000000001
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, pair<int, int>>pi2;
int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };
int res = 0;
int N;
ll x;
vector <ll> v;
ll solve(ll left, ll ret)
{
	ll right = v.size() - 1;
	while (left <= right)
	{
		ll mid = left + right >> 1;
		if (v[mid] == ret) return true;
		if (v[mid] > ret) right = mid - 1;
		else left = mid + 1;
	}
	return false;
}
int main()
{
	ios::sync_with_stdio(false), cin.tie(NULL);	cout.tie(NULL);
	int i;
	ll num;
	while (cin>>x)
	{
		int flag = 0;
		cin >> N;
		x *= 10000000;
		for (i = 0; i < N; i++)
		{
			cin >> num;
			v.push_back(num);
		}
		sort(v.begin(), v.end());
		for (i = 0; i < N - 1; i++)
		{
			ll temp = x - v[i];
			if (solve(i+1,temp))
			{
				cout << "yes " << v[i] << ' ' << temp << '\n';
				flag = 1;
				break;
			}
		}
		if (!flag)cout << "danger\n";
		v.clear();
	}
}