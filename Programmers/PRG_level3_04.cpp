#include <string>
#include <vector>

using namespace std;
long long dp[80];
long long solution(int N) {
    long long answer = 0;
    dp[1]=1;
    dp[2]=1;
    dp[3]=2;
    dp[4]=3;
    dp[5]=5;
    dp[6]=8;
    int i;
    for (i=7;i<=N;i++)
        dp[i]=dp[i-1]+dp[i-2];
    answer=((dp[N]+dp[N-1])*2)+((dp[N-1]+dp[N-2])*2);
    return answer;
}