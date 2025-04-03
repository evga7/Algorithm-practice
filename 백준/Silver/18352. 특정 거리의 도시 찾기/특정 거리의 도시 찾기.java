import java.io.*;
import java.util.*;

public class Main {
    static int N,M,K,X;
    static int res;
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
    static int dp[][];
    static ArrayList<Integer> arr=new ArrayList<>();
    static ArrayList<Integer> g[];
    public static class Info{
        int x,cost;
        public Info(int x, int cost){
            this.x=x;
            this.cost=cost;
        }
    }

    public static void go(int start){
        Queue<Info> q= new LinkedList<>();
        q.add(new Info(start,0));
        dist[start]=0;
        while (!q.isEmpty()){
            var c =q.poll();
            int cur=c.x;
            int cost=c.cost;
            for (var nxt : g[cur]){
                if (dist[nxt]>cost+1){
                    dist[nxt]=cost+1;
                    q.add(new Info(nxt,cost+1));
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        st=new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        K=Integer.parseInt(st.nextToken());
        X=Integer.parseInt(st.nextToken());
        dist=new int [N+1];
        g= new ArrayList[N+1];
        Arrays.fill(dist,987654321);
        for (int i=1;i<=N;i++)
            g[i]=new ArrayList<>();
        for (int i=0;i<M;i++){
            int A,B;
            st=new StringTokenizer(br.readLine());
            A=Integer.parseInt(st.nextToken());
            B=Integer.parseInt(st.nextToken());
            g[A].add(B);
        }
        go(X);
        for (int i=1;i<=N;i++)
        {
            if (dist[i]==K)
                arr.add(i);
        }

        if (arr.isEmpty())
            bw.write("-1");
        else{
            for (var cur : arr)
                bw.write(Integer.toString(cur)+" ");
        }
        bw.close();
    }


}