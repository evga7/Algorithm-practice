import java.io.*;
import java.util.*;

public class Main {
    static int N,M;
    static int res;
    static boolean visited[];
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    static int dx[]={1,0,-1,0};
    static int dy[]={0,1,0,-1};
    static int dp[][];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static ArrayList<String> arr= new ArrayList<>();
    static StringTokenizer st;
    static int p[];
    static int n[];
    public static class Info{
        int x,y;
        Info(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    public static int go(int idx,int s){
        if (idx==M){
            if (s==N)
                return 1;
            return 0;
        }
        if (dp[idx][s]!=-1)
            return dp[idx][s];
        dp[idx][s]=0;
        for (int i=0;i<=n[idx];i++){
            int n_s=s+(p[idx]*i);
            if (n_s<=N)
                dp[idx][s]+=go(idx+1,n_s);
        }
        return dp[idx][s];
    }

    public static void main(String[] args) throws IOException{

        N=Integer.parseInt(br.readLine());
        M=Integer.parseInt(br.readLine());
        p= new int [M+1];
        n= new int [M+1];
        dp=new int [M+1][N+1];
        for (int i=0;i<M;i++)
            Arrays.fill(dp[i],-1);
        for (int i=0;i<M;i++){
            int a,b;
            st=new StringTokenizer(br.readLine());
            p[i]=Integer.parseInt(st.nextToken());
            n[i]=Integer.parseInt(st.nextToken());
        }
        bw.write(Integer.toString(go(0,0)));
        bw.flush();
    }
}