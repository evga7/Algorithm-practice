#include <string>
#include <vector>

using namespace std;

int solution(string s) {
	int len = s.size();
	int answer = len;
	int i,j;
	vector<int> v;
	for (i = 1; i <=s.size()/2; i++)
	{
		string temp = s.substr(0, i);
		string temp2;
		string res;
		int cnt = 1;
		int len2 = temp.size();
		for (j = i; j <=len; j += len2)
		{
			temp2 = s.substr(j,len2);
			if (temp.compare(temp2) == 0)
			{
				cnt++;
			}
			else
			{
				if (cnt == 1)
				{
					res = res + temp;
				}
				else
				{
					res = res + to_string(cnt) + temp;
				}
				temp = temp2;
				cnt = 1;
			}

		}
		
		if (len % i)
		{
			j -= i;
			res = res + s.substr(j,s.size());
		}
		
		int ans2 = res.size();
		answer = min(answer, ans2);
	}

	return answer;
}