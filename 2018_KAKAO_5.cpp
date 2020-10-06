#include <string>
#include <vector>
#include <algorithm>
using namespace std;


int solution(int cacheSize, vector<string> cities) {
	int answer = 0;
	vector<string>s;
	int size = cities.size();
	int i;
	for (i = 0; i < size; i++)
	{
		transform(cities[i].begin(), cities[i].end(), cities[i].begin(), ::tolower);
		auto it = find(s.begin(), s.end(), cities[i]);
		if (it == s.end())
		{
			if (!s.empty()&&s.size() == cacheSize)
			{
				s.erase(s.end()-1);
			}
			answer += 5;
		}
		else
		{
			answer++;
			s.erase(it);
		}
		if (cacheSize!=0)s.insert(s.begin(), cities[i]);
	}
	return answer;
}