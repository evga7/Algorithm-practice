import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static int N,M;
    static int res;
    static int dp[];
    static int visited[][];
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    static int dx[]={1,0,-1,0};
    static int dy[]={0,1,0,-1};
    static ArrayList<Info> arr= new ArrayList<>();
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static class Info{
        int x,y;
        Info(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    public static int go(int idx){
        if (idx==N)
            return 0;
        if (dp[idx]!=-1)
            return dp[idx];
        dp[idx]=0;
        dp[idx]=Math.max(dp[idx],go(idx+1));
        int nxt=idx+arr.get(idx).x;
        int cost=arr.get(idx).y;
        if (nxt<=N)
            dp[idx]=Math.max(dp[idx],go(nxt)+cost);
        return dp[idx];
    }

    public static void main(String[] args) throws IOException{

        N=Integer.parseInt(br.readLine());
        dp= new int[N+1];
        Arrays.fill(dp,-1);
        for (int i=0;i<N;i++){
            int a,b;
            StringTokenizer st = new StringTokenizer(br.readLine());
            a=Integer.parseInt(st.nextToken());
            b=Integer.parseInt(st.nextToken());
            arr.add(new Info(a,b));
        }
        bw.write(Integer.toString(go(0)));
        bw.flush();
    }
}