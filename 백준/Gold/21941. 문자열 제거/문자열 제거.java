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
        if (idx==N)
            return 0;
        if (dp[idx]!=-1)
            return dp[idx];
        dp[idx]=0;
        for (var cur : arr){
            int L=cur.s.length();
            if (idx+L<=N && sb.substring(idx,idx+L).equals(cur.s)){
                dp[idx]=Math.max(dp[idx],go(idx+L)+cur.score);
            }
        }
        dp[idx]=Math.max(dp[idx],go(idx+1)+1);
        return dp[idx];
    }
    static ArrayList<Info> arr=new ArrayList<>();

    public static void main(String[] args) throws IOException {
        sb=new StringBuilder(br.readLine());
        N=sb.length();
        dp = new int [1001];
        Arrays.fill(dp,-1);
        M=Integer.parseInt(br.readLine());
        for (int i=0;i<M;i++){
            st=new StringTokenizer(br.readLine());
            String s;
            int score;
            s=st.nextToken();
            score=Integer.parseInt(st.nextToken());
            if (s.length()>=score)continue;
            arr.add(new Info(s,score));
        }

        bw.write(Integer.toString(go(0)));
        bw.close();
    }


}