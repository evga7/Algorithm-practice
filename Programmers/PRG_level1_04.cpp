#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    int i, j;
    for (i = 0; i < commands.size(); i++)
    {
        vector<int> v;
        for (j = commands[i].at(0)-1; j <commands[i].at(1); j++)
        {
            v.push_back(array.at(j));
        }
        sort(v.begin(), v.end());
        answer.push_back(v.at(commands[i].at(2)-1));
    }
    return answer;
}