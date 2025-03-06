#include <bits/stdc++.h>
#define MAX 987654321
#define MIN -987654321
#define MOD 1000000009
#define pb push_back
#define pob pop_back
#define ms memset
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
int X, Y, K;
int T;
int res;
int num, num2;
int m[21][21];
int dice[4][3];
int temp[4][3];
int d_x, d_y;
bool is_inside(int x, int y)
{
	return x >= 0 && x < N&& y >= 0 && y < M;
}
void copy_dice()
{
	int i, j;
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 3; j++)
		{
			temp[i][j] = dice[i][j];
		}
	}
}
int solve(int dir)
{
	dir--;
	X += dx[dir];
	Y += dy[dir];
	if (!is_inside(X, Y))
	{
		X -= dx[dir];
		Y -= dy[dir];
		return -1;
	}
	copy_dice();
	//동서북남
	//동
	if (dir == 0)
	{
		//6번에 3번넣기
		dice[3][1] = temp[1][2];
		//4번에 6번
		dice[1][0] = temp[3][1];
		dice[1][1] = temp[1][0];
		dice[1][2] = temp[1][1];
	}
	//서
	else if (dir == 1)
	{
		//6번
		dice[3][1] = temp[1][0];
		//4번
		dice[1][0] = temp[1][1];
		//1번
		dice[1][1] = temp[1][2];
		//3번
		dice[1][2] = temp[3][1];
	}
	//북
	else if (dir == 2)
	{
		dice[0][1] = temp[1][1];
		dice[1][1] = temp[2][1];
		dice[2][1] = temp[3][1];
		dice[3][1] = temp[0][1];
	}
	//남
	else if (dir == 3)
	{
		dice[0][1] = temp[3][1];
		dice[1][1] = temp[0][1];
		dice[2][1] = temp[1][1];
		dice[3][1] = temp[2][1];
	}
	if (m[X][Y])
	{
		dice[3][1] = m[X][Y];
		m[X][Y] = 0;
	}
	else
	{
		m[X][Y] = dice[3][1];
	}
	if (dice[1][1])
		return dice[1][1];
	else
		return 0;

}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int i, j;
	cin >> N >> M;
	cin >> X >> Y >> K;
	for (i = 0; i < N; i++)
		for (j = 0; j < M; j++)
			cin >> m[i][j];
	d_x = d_y = 1;
	for (i = 0; i < K; i++)
	{
		cin >> num;
		int t = solve(num);
		if (t != -1)
			cout << t << "\n";
	}
}





