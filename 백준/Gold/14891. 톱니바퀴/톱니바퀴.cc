#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
using namespace std;
typedef long long int ll;
typedef pair<int, int> pi;
typedef pair<int, string> pi3;
typedef pair<int, pair<int, int>>pi2;
typedef pair<int, char> pi4;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };
int N, M;
int num;
int res = 0;
int K;
int m[101][101];
vector<deque<int>>v;
int visited[4];
void spin(int idx, int dir)
{
	if (visited[idx])return;
	visited[idx] = 1;
	int pre = idx - 1;
	int next = idx + 1;
	if (dir == 1)
	{
		if (next <4&&v[next].at(6)!=v[idx].at(2))
			spin(next, dir * -1);
		if (pre >= 0 && v[pre].at(2) !=v[idx].at(6))
			spin(pre, dir * -1);
		int num = v[idx].back();
		v[idx].pop_back();
		v[idx].push_front(num);
	}
	else
	{
		if (next <4 && v[next].at(6) != v[idx].at(2))
			spin(next, dir * -1);
		if (pre >= 0 && v[pre].at(2) != v[idx].at(6))
			spin(pre, dir * -1);
		int num = v[idx].front();
		v[idx].pop_front();
		v[idx].push_back(num);
	}
	return;
}

int solve()
{
	int res = 0;
	int score = 1;
	for (auto num : v)
	{
		if (num.at(0) == 1)
			res += score;
		score *= 2;
	}
	return res;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	int num;
	for (i = 0; i < 4; i++)
	{
		string str;
		deque<int>temp;
		cin >> str;
		for (j=0;j<8;j++)
		temp.push_back(str[j]-'0');
		v.push_back(temp);
	}
	cin >> K;
	for (i = 0; i < K; i++)
	{
		int idx, dir;
		cin >> idx >> dir;
		idx--;
		memset(visited, 0, sizeof(visited));
		spin(idx, dir);
	}
	cout << solve();
}