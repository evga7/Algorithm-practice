import java.io.*;
import java.util.*;

public class Main {
    static int []dx={-1,0,1,0};
    static int [] dy={0,1,0,-1};
    static int N,M,T;
    static int arr[];
    static long dp[][];
    static boolean is_inside(int x,int y,int N,int M)
    {
        return 0<=x&&x<N &&0<=y&&y<M;
    }

    static long go(int N,int M)
    {
        if (N==M || N==0 || M==0)
            return 1;
        if (dp[N][M]!=-1)
            return dp[N][M];
        dp[N][M]=go(N,M-1)+go(N-1,M-1);
        return dp[N][M];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        T=Integer.parseInt(st.nextToken());
        dp=new long[31][31];

        for (int i=0;i<T;i++)
        {
            st=new StringTokenizer(br.readLine());
            int N=Integer.parseInt(st.nextToken());
            int M=Integer.parseInt(st.nextToken());
            for (int j=0;j<=N;j++)
                Arrays.fill(dp[j],-1);
            bw.write(go(N,M)+"\n");
        }
        bw.flush();
    }
}