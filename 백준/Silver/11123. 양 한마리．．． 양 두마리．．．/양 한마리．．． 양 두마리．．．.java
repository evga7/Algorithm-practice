import java.io.*;
import java.sql.Array;
import java.util.*;

public class Main {
    static int dx[]={0,0,1,-1};
    static int dy[]={1,-1,0,0};
    static class Info {
        int x,y;
        Info(int x,int y){
            this.x=x;
            this.y=y;
        }

    }
    public static boolean is_inside(int x,int y,int N,int M)
    {
        return 0<= x && x<N &&0<=y &&y<M;
    }
    static int arr[][];
    static int visited[][];
    static int N,M,K,X;
    static int res;
    public static void go(int sx,int sy)
    {
        Queue<Info> q=new LinkedList<>();
        q.offer(new Info(sx,sy));
        visited[sx][sy]=1;
        while (!q.isEmpty())
        {
            Info a=q.poll();
            int x=a.x;
            int y=a.y;
            for (int i=0;i<4;i++) {
                int n_x = x + dx[i];
                int n_y = y + dy[i];
                if (is_inside(n_x, n_y, N, M) && arr[n_x][n_y] == 1 && visited[n_x][n_y]==0){
                    visited[n_x][n_y] = 1;
                    q.offer(new Info(n_x,n_y));
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T=Integer.parseInt(br.readLine());

        while (T>0)
        {
            res=0;
            T-=1;
            StringTokenizer st= new StringTokenizer(br.readLine());
            N=Integer.parseInt(st.nextToken());
            M=Integer.parseInt(st.nextToken());
            arr=new int [N+1][M+1];
            visited=new int [N+1][M+1];
            for (int i=0;i<N;i++)
            {
                String t=br.readLine();
                for (int j=0;j<M;j++)
                {
                    char c=t.charAt(j);
                    if (c=='#')
                        arr[i][j]=1;
                    else
                        arr[i][j]=0;
                }
            }
            for (int i=0;i<N;i++)
            {
                for (int j=0;j<M;j++)
                {
                    if (arr[i][j]==1 && visited[i][j]==0) {
                        go(i,j);
                        res += 1;
                    }
                }
            }
            bw.write(Integer.toString(res)+"\n");
        }
        bw.flush();

    }

}