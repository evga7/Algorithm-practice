import java.io.*;
import java.util.*;

public class Main {
    static int []dx={-1,0,1,0};
    static int [] dy={0,1,0,-1};
    static int N;
    static int M;
    static char arr[][];
    static boolean visited[][];
    static boolean is_inside(int x,int y,int N,int M)
    {
        return 0<=x&&x<N &&0<=y&&y<M;
    }

    static void go2(int sx,int sy)
    {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{sx,sy});
        while (!q.isEmpty())
        {
            int cur[]=q.poll();
            int x=cur[0];
            int y=cur[1];
            for (int i=0;i<4;i++)
            {
                int n_x=x+dx[i];
                int n_y=y+dy[i];
                if (is_inside(n_x,n_y,N,M)&& arr[n_x][n_y]=='#'&&!visited[n_x][n_y])
                {
                    visited[n_x][n_y]=true;
                    q.offer(new int[]{n_x,n_y});
                }
            }
        }
    }
    static int go()
    {

        int cnt=0;
        for (int i=0;i<N;i++)
        {
            for (int j=0;j<M;j++)
            {
                if (!visited[i][j] &&arr[i][j]=='#')
                {
                    cnt+=1;
                    visited[i][j]=true;
                    go2(i,j);
                }
            }
        }
        return cnt;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T=Integer.parseInt(st.nextToken());
        while (T>0) {
            T-=1;
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            arr=new char[N][M];
            visited=new boolean[N][M];
            for (int i=0;i<N;i++)
            {
                String S=br.readLine();
                for (int j=0;j<M;j++)
                {
                    arr[i][j]=S.charAt(j);
                }
            }
            bw.write(go()+"\n");
        }
        bw.flush();

    }


}