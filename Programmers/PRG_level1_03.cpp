using namespace std;
int arr[31];
int arr2[31];
int solution(int n, vector<int> lost, vector<int> reserve) {
	int answer = 0;
	int i;
	for (i = 0; i < reserve.size(); i++)
		arr[reserve[i]]++;
	for (i = 0; i < lost.size(); i++)
	{
		arr2[lost[i]]++;
	}
	answer = n - lost.size();
	for (i = 0; i <lost.size(); i++)
	{
			if (arr[lost[i]])
			{
			answer++;
			arr[lost[i]]--;
			arr2[lost[i]] = 0;
			}
			else if (arr[lost[i] - 1]&&!arr2[lost[i]-1])
			{
				answer++;
				arr[lost[i] - 1]--;
				arr2[lost[i] - 1] = 0;
			}
			else if (arr[lost[i] + 1]&&!arr2[lost[i] + 1])
			{
				answer++;
				arr[lost[i] + 1]--;
				arr2[lost[i] + 1] = 0;
			}

	}
	return answer;
}