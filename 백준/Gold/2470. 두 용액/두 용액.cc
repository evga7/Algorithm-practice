#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
#define pb push_back
#define pob pop_back
#define ms memset
#define FOR(i,a,b) for(int i = a; i < b; i++)
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pi> vec2;
typedef queue<pi> que;
typedef vector<vector<pi>> gra;
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,1,-1 };
int N, M;
int K;
int T;
ll res;
ll num, num2;
int sum;
string str;
vector<ll>v;
bool cmp(char& c1, char& c2)
{
	return c1 > c2;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	for (i = 0; i < N; i++)
		cin >> num,v.pb(num);
	sort(v.begin(), v.end());
	ll left = 0;
	ll right = N - 1;
	ll s = v[right] + v[left];
	ll res_l=v[left];
	ll res_r=v[right];
	res = 10e15;
	while (left < right)
	{
		if (res > abs(s))
		{
			res = abs(s);
			res_l = v[left];
			res_r = v[right];
		}
		if (s < 0)
			left++;
		else
			right--;
		s = v[right] + v[left];
	}
	cout << res_l << " " << res_r;

}





