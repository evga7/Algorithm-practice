#include <string>
#include <vector>
using namespace std;
vector<int> solution(vector<int> progresses, vector<int> speeds) {
	vector<int> answer;
	int i;
	double arr[101] = { 0 };
	int len = progresses.size();
	for (i = 0; i < len; i++)
	{
		int temp = 100 - progresses[i];
		int temp2 = temp / speeds[i];
		if (progresses[i] + speeds[i] >= 100)
			arr[i] = 1;
		else
		{
			arr[i] = ((double)temp / (double)speeds[i]);
			if (temp2 < arr[i])
				arr[i] = temp2 + 1;
		}
	}
	int cnt = 1;

	double temp = arr[0];
	for (i = 0; i < len-1; i++)
	{
		if (temp>= arr[i + 1])
		{
			cnt++;
		}
		else
		{
			answer.push_back(cnt);
			cnt = 1;
			temp = arr[i + 1];
		}
	}
	answer.push_back(cnt);
	return answer;
}