#include <string>
#include <vector>

using namespace std;

int solution(vector<int> a) {
	int answer = 2;
	int i;
	int l = a[0];
	int len = a.size()-1;
	int r = a[len];
	if (len == 1)
		return 2;
	for (i = 1; i < len; i++)
	{
		if (l>a[i])
		{
			l = a[i];
			answer++;
		}
		if (r > a[len-i])
		{
			r = a[len - i];
			answer++;
		}
	}
	if (l == r) answer--;
	return answer;
}