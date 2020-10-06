#include <string>
#include <math.h>
using namespace std;
bool isbonus(char c)
{
	if (c == '*' || c == '#')
		return true;
	return false;
}
int solution(string dartResult) {
	int answer = 0;
	int size = dartResult.size();
	int i=0;
	int temp = 0;
	int v[4] = { 0 };
	int j = 0;
	for (auto c : dartResult)
	{
		if (isdigit(c))
		{
			if (v[i])
				v[i] *= 10;
			else
			{
				v[i] = c - 48;
			}
		}
		else if (isalpha(c))
		{
			if (c == 'D')
				v[i] = pow(v[i], 2);
			else if (c == 'T')
				v[i] = pow(v[i], 3);
			if (j+1 < size && isdigit(dartResult[j + 1]))
				i++;
		}
		else if (isbonus(c))
		{
			if (c == '*')
			{
				v[i - 1] *= 2;
				v[i] *= 2;
			}
			else if (c == '#')
			{
				v[i] *= -1;
			}
			i++;
		}
		j++;
	}
	for (i = 0; i < 3; i++)
		answer += v[i];
	return answer;
}