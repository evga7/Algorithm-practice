import java.io.*;
import java.util.*;

public class Main {
    static int N,M;
    static int res;
    static int dp[][];
    static int visited[][];
    static char arr[][];
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    public static int go(int x,int y){
        if (!is_inside(x,y,N,M))
            return 1;
        ;
        if (dp[x][y]!=-1)
            return dp[x][y];
        dp[x][y]=0;
        if (arr[x][y]=='D')
            dp[x][y]+=go(x+1,y);
        else if (arr[x][y]=='R')
            dp[x][y]+=go(x,y+1);
        else if (arr[x][y]=='U')
            dp[x][y]+=go(x-1,y);
        else if (arr[x][y]=='L')
            dp[x][y]+=go(x,y-1);
        return dp[x][y];
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st =new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        dp=new int[N][M];
        visited=new int[N][M];
        arr=new char[N][M];
        for (int i=0;i<N;i++){
            st =new StringTokenizer(br.readLine());
            String str=st.nextToken();
            for (int j=0;j<M;j++){
                arr[i][j]=str.charAt(j);
                dp[i][j]=-1;
            }
        }
        for (int i=0;i<N;i++){
            for (int j=0;j<M;j++){
                res+=go(i,j);
            }
        }
        bw.write(Integer.toString(res));
        bw.flush();
    }
}