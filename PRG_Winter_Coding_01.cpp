#include <string>
#include <vector>

using namespace std;
int solution(string skill, vector<string> skill_trees) {
	int answer = 0;
	int i, j, k;
	for (i=0;i<skill_trees.size();i++)
	{
		int pos = 0;
		int flag = 0;
		for (j=0;j<skill_trees[i].size();j++)
		{
			for (k=0;k<skill.size();k++)
			{
				flag = 0;
				if (skill_trees[i][j] == skill[k])
				{
					if (pos == k)
					{
						pos++;
						break;
					}
					else
						flag = 1;
				}
				if (flag)
					break;
			}
			if (flag)
				break;
		
		}
		if (flag == 0)
			answer++;
	}
	printf("%d", answer);
	return answer;
}