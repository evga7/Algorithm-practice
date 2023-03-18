#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int solution(string str1, string str2) {
	int answer = 0;
	int i;
	string s1, s2;
	for (auto s : str1)
	{
		if (s >= 'A' && s <= 'Z')
			s1 = s1 + s;
		else if (s >= 'a' && s <= 'z')
		{
			s -= 32;
			s1 = s1 + s;
		}
		else
			s1 = s1 + s;
	}
	for (auto s : str2)
	{
		if (s >= 'A' && s <= 'Z')
			s2 = s2 + s;
		else if (s >= 'a' && s <= 'z')
		{
			s -= 32;
			s2 = s2 + s;
		}
		else
			s2 = s2 + s;
	}
	vector<string>v1, v2,v3,v4;
	for (i = 0; i < s1.size() - 1; i++)
	{
		string temp;
		if (s1[i] >= 'A' && s1[i] <= 'Z' && s1[i + 1] >= 'A' && s1[i + 1] <= 'Z')
		{
			temp = temp + s1[i] + s1[i + 1];
			v1.push_back(temp);
		}
	}
	for (i = 0; i < s2.size() - 1; i++)
	{
		string temp;
		if (s2[i] >= 'A' && s2[i] <= 'Z' && s2[i + 1] >= 'A' && s2[i + 1] <= 'Z')
		{
			temp = temp + s2[i] + s2[i + 1];
			v2.push_back(temp);
		}
	}
	v3.resize(v1.size() + v2.size());
	v4.resize(v1.size() + v2.size());
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	auto iter=set_union(v1.begin(), v1.end(), v2.begin(), v2.end(),v3.begin());
	v3.erase(iter, v3.end());
	auto iter2 = set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), v4.begin());
	v4.erase(iter2, v4.end());
    	if (v3.size() == 0)
		return 65536;
	answer= ((double)v4.size() / (double)v3.size()) * 65536;
	return answer;
}