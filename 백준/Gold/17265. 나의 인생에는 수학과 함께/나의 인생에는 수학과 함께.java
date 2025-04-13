import java.io.*;
import java.util.*;

public class Main {
    static int N,M,K,X;
    static int res;
    static int res2;
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    static int dx[]={1,0,-1,0};
    static int dy[]={0,1,0,-1};
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static StringBuilder sb;
    static int dist[];
    static int dp[][][];
    static char arr[][];
    static ArrayList<Integer> g[];

    public static void solve(int x,int y,int op,int num) {
        if (x==N-1 && y==N-1)
        {
            if (op==0) {
                res = Math.max(res, num+(arr[x][y]-'0'));
                res2 = Math.min(res2, num+(arr[x][y]-'0'));
            }
            else if (op==1) {
                res = Math.max(res, num*(arr[x][y]-'0'));
                res2 = Math.min(res2, num*(arr[x][y]-'0'));
            }
            else {
                res = Math.max(res, num-(arr[x][y]-'0'));
                res2 = Math.min(res2, num-(arr[x][y]-'0'));
            }
            return;
        }
        for (int i=0;i<2;i++){
            int n_x=x+dx[i];
            int n_y=y+dy[i];
            if (is_inside(n_x,n_y,N,N)){
                if (Character.isDigit(arr[x][y])){
                    if (op==0)
                        solve(n_x,n_y,0,num+(arr[x][y]-'0'));
                    else if (op==1)
                        solve(n_x,n_y,0,num*(arr[x][y]-'0'));
                    else
                        solve(n_x,n_y,0,num-(arr[x][y]-'0'));
                }
                else{
                    if (arr[x][y]=='+')
                        solve(n_x,n_y,0,num);
                    else if (arr[x][y]=='*')
                        solve(n_x,n_y,1,num);
                    else
                        solve(n_x,n_y,2,num);
                }
            }

        }

    }
    public static void main(String[] args) throws IOException {
        N=Integer.parseInt(br.readLine());
        res=-987654321;
        res2=987654321;
        dp =new int [N+1][N+1][3];
        arr =new char [N+1][N+1];
        for (int i=0;i<N;i++) {
            st=new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++)
            {
                arr[i][j]=st.nextToken().charAt(0);
            }
        }


        for (int i=0;i<N;i++)
            for (int j=0;j<N;j++)
                Arrays.fill(dp[i][j],-1);
        solve(0,0,0,0);
        bw.write(Integer.toString(res)+"\n"+Integer.toString(res2));
        bw.close();
    }


}