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
    static ArrayList<Integer> arr =new ArrayList<>();
    static int b[];
    public static class Info{
        String s;
        int score;
        public Info(String s,int score){
            this.score=score;
            this.s=s;
        }
    }
    public static int go(int cnt,int idx){
        if (idx==N || cnt==3)
            return 0;
        if (dp[cnt][idx]!=-1)
            return dp[cnt][idx];
        int ret=0;
        int right=Math.min(N,idx+M);
        if (right<=N)
            ret=Math.max(ret,go(cnt+1,right)+(b[right]-b[idx]));
        ret=Math.max(ret,go(cnt,idx+1));
        dp[cnt][idx]=ret;
        return dp[cnt][idx];

    }

    public static void main(String[] args) throws IOException {
        N=Integer.parseInt(br.readLine());
        st=new StringTokenizer(br.readLine());
        b=new int [N+1];
        dp=new int [3][N+1];
        for (int i=0;i<3;i++)
            Arrays.fill(dp[i],-1);
        for (int i=0;i<N;i++){
            arr.add(Integer.parseInt(st.nextToken()));
        }
        for (int i=1;i<=N;i++){
            b[i]=arr.get(i-1)+b[i-1];
        }
        M=Integer.parseInt(br.readLine());
        bw.write(Integer.toString(go(0,0)));
        bw.close();
    }


}