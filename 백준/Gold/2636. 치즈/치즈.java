import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int []dx={-1,0,1,0};
    static int [] dy={0,1,0,-1};
    static boolean is_inside(int x,int y,int N,int M)
    {
        return 0<=x&&x<N &&0<=y&&y<M;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        int [][] a=new int[N][M];


        for (int i=0;i<N;i++)
        {
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<M;j++) {
                a[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int res=0;
        int res2=0;
        while(true) {
            PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[0] - o2[0]);;
            pq.offer(new int[]{0,0});
            boolean [][] visited=new boolean[N][M];
            visited[0][0]=true;
            int cnt=0;
            while (!pq.isEmpty()) {
                int x, y;
                int cur[] = pq.poll();
                x = cur[0];
                y = cur[1];
                for (int i = 0; i < 4; i++) {
                    int n_x = x + dx[i];
                    int n_y = y + dy[i];
                    if (is_inside(n_x,n_y,N,M) && !visited[n_x][n_y])
                    {
                        visited[n_x][n_y]=true;
                        if (a[n_x][n_y]==1)
                        {
                            cnt+=1;
                            a[n_x][n_y]=0;
                            continue;
                        }
                        pq.offer(new int[]{n_x,n_y});
                    }
                }
            }

            if (cnt==0)
            {
                break;
            }
            res+=1;
            res2=cnt;
        }
        bw.write(String.valueOf(res+"\n"+res2));
        bw.flush();
    }


}