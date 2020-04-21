#include <string>
#include <vector>

using namespace std;

bool chk(string s)
{
	int i = 0;
	int cnt = 0;
	for (i = 0; i < s.size(); i++)
	{
		if (s[i] == '(')
			cnt++;
		else
			cnt--;
		if (cnt < 0)
			return false;
	}
	if (cnt==0)
		return true;
	return false;
}

string solution(string s) {
	string answer = "";
	if (chk(s)) return s;
	string u, v;
	int i;
	int L, R = 0;
	L = R = 0;
	for (i = 0; i < s.size(); i++)
	{
		if (s[i] == '(')
			L++;
		else
			R++;
		if (L == R)
			break;
	}
	u = s.substr(0, i+1);
	v = s.substr(i+1, s.size() - (i+1));
	if (chk(u))
	{
		return u + solution(v);
	}
	
	answer = "(" + solution(v) + ")";
	for (i = 1; i < u.size()-1; i++)
	{
		if (u[i] == '(')
			answer += ')';
		else
			answer+='(';
	}

	return answer;
}