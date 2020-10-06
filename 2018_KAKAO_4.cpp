#include <cstring>
#include <vector>
#include <string>
using namespace std;
int N, M;
int arr[31][31];
bool chk(int x, int y, vector<string>board)
{
    char c = board[x][y];
    if (x + 1 >= N || y + 1 >= M||c==33)
        return false;
    if (board[x + 1][y] == c && board[x][y + 1] == c && board[x + 1][y + 1] == c)
    {
        arr[x][y]=arr[x + 1][y] = arr[x][y + 1] = arr[x + 1][y + 1] = 1;
        return true;
    }
    return false;
}
int solution(int m, int n, vector<string> board) {
    int answer = 0;
    N = m;
    M = n;
    int i, j;
    int flag = 0;
    while (1)
    {
        memset(arr, 0, sizeof(arr));
        for (i = 0; i < N; i++)
        {
            for (j = 0; j < M; j++)
            {
                if (chk(i, j, board))flag = 1;
            }
        }
        if (flag == 0)
            break;
        else
        {
            for (i = 0; i < N; i++)
                for (j = 0; j < M; j++)
                    if (arr[i][j] == 1)
                        board[i][j] = 33;
            for (j = 0; j < M; j++)
            {
                for (i = N - 1; i >= 0; i--)
                {
                    if (board[i][j] == 33)
                    {
                        int x = i;
                        int y = j;
                        while (1)
                        {
                            x--;
                            if (arr[x][y] == 0||x<0)
                                break;
                        }
                        if (x >= 0)
                        {
                            arr[x][y] = 1;
                            board[i][j] = board[x][y];
                            board[x][y] = 33;
                        }
                        else
                            break;
                    }
                }
            }
        }
        flag = 0;
    }
    for (i = 0; i < N; i++)
        for (j = 0; j < M; j++)
            if (board[i][j] == 33)
                answer++;
    return answer;
}