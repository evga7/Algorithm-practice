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
    static int dp[];
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
    public static int go(int idx){
        if (idx==N-1)
            return 0;
        if (dp[idx]!=-1)
            return dp[idx];
        int ret=987654321;
        for (int i=idx+1;i<N;i++)
        {
            int p=i-idx;
            int pp=p*p;
            if (sb.charAt(idx)=='B' &&sb.charAt(i)=='O'){
                ret=Math.min(ret,go(i)+pp);
            }
            if (sb.charAt(idx)=='O'&&sb.charAt(i)=='J'){
                ret=Math.min(ret,go(i)+pp);
            }
            if (sb.charAt(idx)=='J'&&sb.charAt(i)=='B'){
                ret=Math.min(ret,go(i)+pp);
            }
        }
        dp[idx]=ret;
        return dp[idx];

    }

    public static void main(String[] args) throws IOException {
        N=Integer.parseInt(br.readLine());
        sb=new StringBuilder(br.readLine());
        dp=new int [1001];
        Arrays.fill(dp,-1);
        int res=go(0);
        if (res==987654321)
            res=-1;
        bw.write(Integer.toString(res));
        bw.close();
    }


}