import java.util.*;
class Solution {
    static int mod=1000000007;
    static int [][]dp=new int[101][101];
    static int N,M;
    static int [][]p=new int[101][101];
    public int go(int x,int y)
    {
        if (x>N || y>M || p[x][y]==1)return 0;
        if (x==N&&y==M)
            return 1;
        if (dp[x][y]!=-1)
            return dp[x][y];
        int ret=0;
        ret+=(go(x+1,y)+go(x,y+1))%mod;
        return dp[x][y]=ret;
    }
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        for (int i=0;i<=n;i++)
        {
            Arrays.fill(dp[i],-1);
        }
        for (int i=0;i<puddles.length;i++)
        {
            int x,y;
            x=puddles[i][1];
            y=puddles[i][0];
            p[x][y]=1;
        }
        N=n;
        M=m;
        return go(1,1);
    }
}