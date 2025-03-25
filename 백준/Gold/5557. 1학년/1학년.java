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
    static long dp[][];
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
    public static long go(int idx,int s){
        if (idx==N-1)
        {
            if (arr.get(idx)==s)
                return 1;
            return 0;
        }
        if (dp[idx][s]!=-1) {
            return dp[idx][s];
        }
        dp[idx][s]=0;
        int nxt=s+arr.get(idx);
        int nxt2=s-arr.get(idx);
        if (0<=nxt && nxt<=20)
            dp[idx][s]+=go(idx+1,s+arr.get(idx));
        if (0<=nxt2 && nxt2<=20)
            dp[idx][s]+=go(idx+1,s-arr.get(idx));
        return dp[idx][s];
    }
    static ArrayList<Integer> arr=new ArrayList<>();

    public static void main(String[] args) throws IOException {
        N=Integer.parseInt(br.readLine());
        st=new StringTokenizer(br.readLine());
        dp=new long [N+1][21];
        for (int i=0;i<N;i++)
            Arrays.fill(dp[i],-1);
        for (int i=0;i<N;i++)
            arr.add(Integer.parseInt(st.nextToken()));
        bw.write(Long.toString(go(1,arr.get(0))));
        bw.close();
    }


}