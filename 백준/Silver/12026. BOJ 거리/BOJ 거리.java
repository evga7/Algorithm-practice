import java.io.*;
import java.util.*;

public class Main {
    static int N,M;
    static int res;
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    static int dx[]={1,0,-1,0};
    static int dy[]={0,1,0,-1};
    static int dp[][];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static StringBuilder sb;
    public static class Info{
        String s;
        int score;
        public Info(String s,int score){
            this.score=score;
            this.s=s;
        }
    }
    public static int go(int idx,int op){
        if (idx==N-1)
            return 0;
        if (dp[idx][op]!=-1)
            return dp[idx][op];
        dp[idx][op]=987654321;
        for (int i=idx+1;i<N;i++)
        {
            int p=i-idx;
            int pp=p*p;
            if (op==0 &&sb.charAt(i)=='O'){
                dp[idx][op]=Math.min(dp[idx][op],go(i,1)+pp);
            }
            if (op==1 &&sb.charAt(i)=='J'){
                dp[idx][op]=Math.min(dp[idx][op],go(i,2)+pp);
            }
            if (op==2 &&sb.charAt(i)=='B'){
                dp[idx][op]=Math.min(dp[idx][op],go(i,0)+pp);
            }
        }
        return dp[idx][op];

    }

    public static void main(String[] args) throws IOException {
        N=Integer.parseInt(br.readLine());
        sb=new StringBuilder(br.readLine());
        dp=new int [1001][3];
        for (int i=0;i<1000;i++)
            Arrays.fill(dp[i],-1);
        int res=go(0,0);
        if (res==987654321)
            res=-1;
        bw.write(Integer.toString(res));
        bw.close();
    }


}