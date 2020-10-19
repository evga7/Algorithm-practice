#include <bits/stdc++.h>
using namespace std;
int visited[10];
set<string>s;
int res=0;
bool chk(string a, string b)
{
	if (a.size() != b.size())
		return false;
	int i;
	for (i = 0; i < a.size(); i++)
	{
		if (a[i] == '*' || b[i] == '*')continue;
		if (a[i] != b[i])return false;
	}
	return true;
}
void dfs(vector<string>& user_id, vector<string>& banned_id, int cnt,string S)
{
	int size = banned_id.size();
	int size2 = user_id.size();
	if (cnt == size)
	{
		sort(S.begin(), S.end());
		if (s.find(S) == s.end())
		{
			s.insert(S);
			res++;
		}
		return;
	}
	int i;
	for (i = 0; i < size2; i++)
	{
		if (visited[i])continue;
		string temp = banned_id[cnt];
		if (chk(temp, user_id[i]))
		{
			visited[i] = 1;
			dfs(user_id, banned_id, cnt + 1,S+to_string(i));
			visited[i] = 0;
		}
	}

}
int solution(vector<string> user_id, vector<string> banned_id) {
	int answer = 0;
	dfs(user_id, banned_id, 0,"");
	return res;
}