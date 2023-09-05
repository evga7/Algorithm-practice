import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static int []dx={-1,0,1,0};
    static int [] dy={0,1,0,-1};
    static int N,M,T,K;
    static int arr[][]= new int [21][2];
    static int visited[];
    static BufferedReader br;
    static BufferedWriter bw;
    static StringTokenizer st;
    static boolean is_inside(int x,int y,int N,int M)
    {
        return 0<=x&&x<N &&0<=y&&y<M;
    }

    static int[][] dp =new int[21][2];
    public static int go(int idx,int cnt)
    {
        if (idx>=N)
            return 987654321;
        if (idx==N-1)
            return 0;
        if (dp[idx][cnt]!=-1)
            return dp[idx][cnt];
        dp[idx][cnt]=987654321;
        dp[idx][cnt]=Math.min(dp[idx][cnt],Math.min(go(idx+1,cnt)+arr[idx][0],go(idx+2,cnt)+arr[idx][1]));
        if (cnt==0)
            dp[idx][cnt]=Math.min(dp[idx][cnt],go(idx+3,1)+K);
        return dp[idx][cnt];
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        st = new StringTokenizer(br.readLine());
        N= Integer.parseInt(st.nextToken());

        for (int i=0;i<=N;i++)
            Arrays.fill(dp[i],-1);
        for (int i=0;i<N-1;i++)
        {
            st=new StringTokenizer(br.readLine());
            int num= Integer.parseInt(st.nextToken());
            int num2= Integer.parseInt(st.nextToken());
            arr[i][0]=num;
            arr[i][1]=num2;
        }
        st=new StringTokenizer(br.readLine());
        K= Integer.parseInt(st.nextToken());
        bw.write(String.valueOf(go(0,0)));
        bw.flush();



    }
}