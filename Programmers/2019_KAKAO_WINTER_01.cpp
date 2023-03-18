#include <string>
#include <vector>
#include <stack>
using namespace std;
int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    int i;
    int size = board.size();
    stack<int>s;
    for (auto num : moves)
    {
        int idx = size-1;
        
        while (idx>=0&&board[idx][num - 1])
        {
            idx--;
        }
        if (idx+1<size)
            idx++;
        int& ret = board[idx][num - 1];
        if (ret != 0)
        {
            if (s.empty())
                s.push(ret);
            else
            {
                if (s.top() == ret)
                {
                    s.pop();
                    answer++;
                }
                else
                    s.push(ret);
            }
            ret = 0;
        }
    }
    return answer*2;
}