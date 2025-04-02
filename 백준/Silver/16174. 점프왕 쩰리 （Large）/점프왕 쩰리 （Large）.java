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
    static int arr[][];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static StringBuilder sb;
    static int b[];
    static int dp[][];
    public static class Info{
        String s;
        int score;
        public Info(String s,int score){
            this.score=score;
            this.s=s;
        }
    }
    public static int go(int x,int y){
        if (x==N-1 && y==N-1){
            return 1;
        }
        if (dp[x][y]!=-1)
            return dp[x][y];
        dp[x][y]=0;
        int cur=arr[x][y];
        for (int i=0;i<2;i++) {
            int n_x=x+(dx[i]*cur);
            int n_y=y+(dy[i]*cur);
            if (is_inside(n_x,n_y,N,N))
                dp[x][y]=Math.max(dp[x][y],go(n_x,n_y));
        }
        return dp[x][y];

    }

    public static void main(String[] args) throws IOException {
        N=Integer.parseInt(br.readLine());

        dp =new int [N+1][N+1];
        arr =new int [N+1][N+1];
        for (int i=0;i<N;i++){
            Arrays.fill(dp[i],-1);
            st=new StringTokenizer(br.readLine());
            for (int j=0;j<N;j++)
                arr[i][j]=Integer.parseInt(st.nextToken());
        }
        res=go(0,0);
        if (res>0)
            bw.write("HaruHaru");
        else
            bw.write("Hing");
        bw.close();
    }


}