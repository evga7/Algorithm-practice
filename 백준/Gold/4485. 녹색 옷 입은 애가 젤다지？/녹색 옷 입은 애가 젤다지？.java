import java.io.*;
import java.sql.Array;
import java.util.*;

public class Main {
    static int dx[]={0,0,1,-1};
    static int dy[]={1,-1,0,0};
    static class Info implements Comparable<Info> {
        int x,y,cost;
        public Info(int x,int y,int cost){
            this.x=x;
            this.y=y;
            this.cost=cost;
        }
        @Override
        public int compareTo(Info o)
        {
            return this.cost-o.cost;
        }

    }
    public static boolean is_inside(int x,int y,int N,int M)
    {
        return 0<= x && x<N &&0<=y &&y<M;
    }
    static int arr[][];
    static int dist[][];
    static int N,M,K,X;
    public static void main(String[] args) throws IOException {
        X=0;
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        while (true)
        {
            X+=1;
            N=Integer.parseInt(br.readLine());
            if (N==0)
                break;
            arr=new int[N+1][N+1];
            dist=new int[N+1][N+1];
            for (int i=0;i<N+1;i++)
                Arrays.fill(dist[i],987654321);
            for (int i=0;i<N;i++)
            {
                StringTokenizer st=new StringTokenizer(br.readLine());
                for (int j=0;j<N;j++)
                {
                    arr[i][j]=Integer.parseInt(st.nextToken());
                }
            }
            PriorityQueue<Info> q= new PriorityQueue<>();
            q.add(new Info(0,0,arr[0][0]));
            dist[0][0]=arr[0][0];
            while (!q.isEmpty())
            {
                Info info=q.poll();
                int x=info.x,y=info.y,cost=info.cost;
                if (dist[x][y]<cost)continue;
                for (int i=0;i<4;i++)
                {
                    int n_x=x+dx[i];
                    int n_y=y+dy[i];
                    if (is_inside(n_x,n_y,N,N) && dist[n_x][n_y]>cost+arr[n_x][n_y])
                    {
                        dist[n_x][n_y]=cost+arr[n_x][n_y];
                        q.add(new Info(n_x,n_y,cost+arr[n_x][n_y]));
                    }
                }
            }
            System.out.println("Problem " + X + ": " + dist[N-1][N-1]);
        }
    }
}