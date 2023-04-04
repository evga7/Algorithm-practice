#include <bits/stdc++.h>
using namespace std;
int dp[20001];
vector<string>strs2;
int t_size;
string t2;
int solve(int idx)
{
	if (idx == t2.size())return 0;
	int& ret = dp[idx];
	int i, j;
	if (ret!=-1)return ret;
	ret = 987654321;
	for (i = 0; i < strs2.size(); i++)
	{
		int S = strs2[i].size();
		int flag = 0;

		if (S + idx <=t_size)
		{
			for (j = 0; j < S; j++)
			{
				if (strs2[i][j] != t2[idx + j])
				{
					flag = 1;
					break;
				}
			}
			if (!flag)
			{
				ret = min(ret, solve(idx + S) + 1);
			}
		}
	}
	return ret;
}
int solution(vector<string> strs, string t)
{
	int answer = 0;
	strs2 = strs;
	t_size = t.size();
	memset(dp, -1, sizeof(dp));
	t2 = t;
	answer = solve(0);
    if (answer==987654321)return -1;
	return answer;
}