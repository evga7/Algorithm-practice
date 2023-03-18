#include <string>
#include <vector>
#include <iostream>
#include <set>
#include <map>
using namespace std;
int m[11][11][11][11];
int dx[4] = { 0,-1,0,1 };
int dy[4] = { -1,0,1,0 };
int chk_op(char op)
{
	if (op == 'L')
		return 0;
	else if (op == 'U')
		return 1;
	else if (op == 'R')
		return 2;
	else
		return 3;
}
int solution(string dirs)
{
	int answer = 0;
	int i;
	int x = 5, y = 5;
	for (i = 0; i < dirs.size(); i++)
	{
		int op = chk_op(dirs[i]);
		int n_x, n_y;
		n_x = x + dx[op];
		n_y = y + dy[op];
		if (n_x < 0 || n_x>10 || n_y < 0 || n_y>10)
			continue;
		if (!m[x][y][n_x][n_y])
		{
			m[x][y][n_x][n_y] = 1;
			m[n_x][n_y][x][y] = 1;
			answer++;
		}
		x = n_x;
		y = n_y;
	}
	cout << answer;
	return answer;
}