#include <bits/stdc++.h>
#include<unordered_map>
#define MAX 1000000001
#define MIN -987654321
#define MOD 1000000009
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
int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };
int N, M;
int T;
int K;
int res;
int num, num2;
deque<int>belt;
deque<int>life;
void rotate()
{
	belt.push_front(belt.back());
	belt.pop_back();
	belt[N - 1] = 0;
	life.push_front(life.back());
	life.pop_back();
}
void move()
{
	int i;
	for (i = N - 2; i >= 0; i--)
	{
		if (life[i+1] && !belt[i+1] && belt[i])
		{
			life[i+1]--;
			belt[i+1] = 1;
			belt[i] = 0;
		}
	}
	belt[N - 1] = 0;
}
void robot()
{
	if (!belt[0] && life[0])
	{
		belt[0] = 1;
		life[0]--;
	}
}
void solve()
{
	int cnt = 0;
	while (1)
	{
		cnt = 0;
		res++;
		rotate();
		move();
		robot();
		for (auto a : life)
		{
			if (!a)cnt++;
		}
		if (cnt >= K)
			break;
	}
	cout << res;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> K;
	belt.resize(2 * N);
	life.resize(2 * N);
	for (i = 0; i <2*N; i++)
	{
		cin >> life[i];
	}
	solve();
}





