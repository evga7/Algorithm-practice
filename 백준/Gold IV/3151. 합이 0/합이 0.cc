#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000007
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
int dx[4] = { 0, 0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int N, M, T;
int S;
ll res;
int num, num2;
int arr[10001];
void solve()
{
	int i, j;
	for (i = 0; i < N - 2; i++)
	{
		for (int j = i+1; j < N - 1; j++)
		{
			int s = -(arr[i] + arr[j]);
			res +=upper_bound(arr+j+1,arr+N,s)-lower_bound(arr + j + 1, arr + N, s);
		}
	}
	cout << res;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N;
	for (i = 0; i < N; i++)
	{
		cin >> arr[i];
	}
	sort(arr, arr + N);
	solve();
}