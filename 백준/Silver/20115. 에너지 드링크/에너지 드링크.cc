#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 987654321
#define MIN -987654321
#define MOD  1000000009
#define pb push_back
#define pob pop_back
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef pair<int, int> pii;
typedef pair<string, int> psi;
typedef pair<int, string> pis;
typedef vector<vector<int>> vvec;
typedef vector<int> vec;
typedef vector<ll> vecll;
typedef vector<pii> vpi;
typedef vector<pii> vec2;
typedef vector<vector<pii>> gra;
double res;
int N, M, T;
double num;
string str;
//아래 왼쪽 오른 위
int dx[4] = { 1,0,0,-1 };
int dy[4] = { 0,-1,1,0 };
vector<double>v;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}
	sort(v.begin(), v.end());
	res = v[N - 1];
	for (int i = 0; i < N-1; i++)
	{
		res += v[i] / 2;
	}
	cout << res;
}



