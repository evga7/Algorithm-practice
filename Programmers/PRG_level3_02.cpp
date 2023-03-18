#include <string>
#include <vector>
using namespace std;
int arr[102][102]={0};
int dp[102][102]={0};

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    int i,j;
    for (auto A:puddles)
        arr[A[1]][A[0]]=1;
    dp[1][0]=1;
    for (i=1;i<=n;i++)
    {        
        for (j=1;j<=m;j++)
        {
            if (arr[i][j]==1)
                dp[i][j]=0;
            else
                dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000000007;
        }
                    
    }
    answer=dp[n][m];
    return answer;
}