#include <string>
#include <vector>
#include <iostream>
#include <set>
using namespace std;
set<string>s;
vector<int> solution(int n, vector<string> words) {
	vector<int> answer;
	int i;
	char back;
	back = 0;
	int a, b;
	a = b = 0;
	for (i = 0; i < words.size(); i++)
	{
		if (s.find(words[i]) == s.end())
		{
			if (i != 0)
			{
				if (back != words[i].front())
				{
					a = (i%n)+1;
			        b = (i/n)+1;
					break;
				}
			}
			s.insert(words[i]);
		}
		else {
			a = (i%n)+1;
			b = (i/n)+1;
			break;
		}
		back = words[i].back();
	}
	return { a,b };
}