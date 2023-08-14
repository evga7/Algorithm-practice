import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int []dx={-1,0,1,0};
    static int [] dy={0,1,0,-1};
    static int N;
    static int M;
    static int [][]visited=new int[501][501];
    static int [][]a=new int[501][501];
    static int sx,sy,ex,ey,A,B;
    static boolean is_inside(int x,int y,int N,int M)
    {
        return 0<x&&x<=N &&0<y&&y<=M;
    }
    static boolean is_inside2(int x,int y,int A,int B)
    {
        for (int i=x;i<x+A;i++)
        {
            for (int j=y;j<y+B;j++)
            {
                if (is_inside(i,j,N,M)==false || a[i][j]==1)
                    return false;
            }
        }
        return true;
    }
    public static int go()
    {
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[0]-o2[0]);
        pq.offer(new int[]{0,sx,sy});
        visited[sx][sy]=1;
        while (!pq.isEmpty())
        {
            int cost,x,y;
            int cur[]=pq.poll();
            cost=cur[0];
            x=cur[1];
            y=cur[2];
            if (x==ex && y==ey)
            {
                return cost;
            }
            for (int i=0;i<4;i++)
            {
                int n_x=x+dx[i];
                int n_y=y+dy[i];

                if (is_inside2(n_x,n_y,A,B) && visited[n_x][n_y]==0)
                {
                    visited[n_x][n_y]=1;
                    pq.offer(new int[]{cost+1,n_x,n_y});
                }
            }

        }
        return -1;
    }
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        A=Integer.parseInt(st.nextToken());
        B=Integer.parseInt(st.nextToken());
        int K=Integer.parseInt(st.nextToken());
        for (int i=0;i<K;i++)
        {
            st=new StringTokenizer(br.readLine());
            int x=Integer.parseInt(st.nextToken());
            int y=Integer.parseInt(st.nextToken());
            a[x][y]=1;
        }
        st=new StringTokenizer(br.readLine());
        sx=Integer.parseInt(st.nextToken());
        sy=Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());
        ex=Integer.parseInt(st.nextToken());
        ey=Integer.parseInt(st.nextToken());

        bw.write(String.valueOf(go()));
        bw.flush();
    }


}