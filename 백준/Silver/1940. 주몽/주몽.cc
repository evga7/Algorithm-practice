#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef vector<vector<int>> vvi;
typedef vector<pii>vpi;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef queue<pii> que;
typedef vector<vector<pii>> gra;
int dx[4] = { 0,1,0,-1 }; //오 아래 왼 위
int dy[4] = { 1,0,-1,0 };
int res;
int num;
string str;
int N, M;
vec v;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N >> M;
	for (int i = 0; i < N; ++i)
	{
		cin >> num, v.push_back(num);
	}
	sort(v.begin(), v.end());
	int left = 0;
	int right = N - 1;
	while (left < right)
	{
		int mid = v[left] + v[right];
		if (mid >= M)
		{
			if (mid == M)res++;
			right--;
		}
		else
			left++;
	}
	cout << res;
	
}