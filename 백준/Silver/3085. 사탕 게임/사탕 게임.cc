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
int N, M;
char arr[51][51];
void chk()
{
	int c = 0;
	for (int i = 0; i < N; i++)
	{
		int cnt1 = 1;
		int cnt2 = 1;
		int idx1 = 0;
		int idx2 = 0;
		while (idx1 < N - 1)
		{
			if (arr[idx1][i] == arr[idx1 + 1][i])
				cnt1++;
			else
			{
				res = max(res, cnt1);
				cnt1 = 1;
			}
			idx1++;
		}
		while (idx2 < N - 1)
		{
			if (arr[i][idx2] == arr[i][idx2 + 1])
				cnt2++;
			else
			{
				res = max(res, cnt2);
				cnt2 = 1;
			}
			idx2++;
		}
		c = max({cnt1, cnt2, c});
	}
	res = max(res, c);
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin>>arr[i][j];
		}
	}
	chk();
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (arr[i][j] != arr[i][j + 1]&&j+1<N)
			{
				swap(arr[i][j], arr[i][j + 1]);
				chk();
				swap(arr[i][j], arr[i][j + 1]);
			}
			if (arr[i][j] != arr[i + 1][j]&&i+1)
			{
				swap(arr[i][j], arr[i + 1][j]);
				chk();
				swap(arr[i][j], arr[i + 1][j]);
			}
		}
	}
	cout << res;
}