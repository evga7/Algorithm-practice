#include <string>
#include <vector>

using namespace std;
vector<int> solution(vector<int> answers) {
	vector<int> answer;
	int i;
	int stu1[5] = { 1,2,3,4,5 };
	int stu2[8] = { 2, 1, 2, 3, 2, 4, 2, 5, };
	int stu3[10] = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };
	int val[3]={0,0,0};
	for (i = 0; i < answers.size(); i++)
	{
		if (stu1[i % 5] == answers[i])
			val[0]++;
		if (stu2[i % 8] == answers[i])
			val[1]++;
		if (stu3[i % 10] == answers[i])
			val[2]++;
	}
    int MAX=max(max(val[0],val[1]),val[2]);
    for (i=0;i<3;i++)
        if (MAX==val[i])
            answer.push_back(i+1);
	return answer;
}