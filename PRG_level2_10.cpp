#include <vector>
#include <set>
using namespace std;
int solution(vector<int> nums)
{
	int answer = 0;
	set<int>s;
	int Size = nums.size();
	for (auto num : nums)
	{
		if (s.find(num) == s.end())
			s.insert(num);
	}
	if (Size / 2 <= s.size())
		answer = Size / 2;
	else
		answer = s.size();
	return answer;
}