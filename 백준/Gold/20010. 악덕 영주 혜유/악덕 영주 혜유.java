import java.io.*;
import java.util.*;

public class Main {
    static int N,M;
    static int res;
    static boolean visited[];
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    static int dx[]={1,0,-1,0};
    static int dy[]={0,1,0,-1};
    static int dp[][];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static ArrayList<Integer> arr= new ArrayList<>();
    static StringTokenizer st;
    static ArrayList<Info> g =new ArrayList<>();
    static ArrayList<Info> g2[];
    static int p[];
    static int dist[];
    public static class Info implements Comparable<Info>{
        int x,y,cost;
        Info(int x,int y,int cost){
            this.x=x;
            this.y=y;
            this.cost=cost;
        }
        @Override
        public int compareTo(Info o){
            return Integer.compare(this.cost,o.cost);
        }

    }
    public static int find(int x){
        if (x==p[x])
            return x;
        return p[x]=find(p[x]);
    }
    public static boolean uni(int x,int y){
        x=find(x);
        y=find(y);
        if (x!=y){
            if (x<y)
                p[y]=x;
            else
                p[x]=y;
            return true;
        }
        return false;
    }
    private static void go(int start) {
        Queue<Info> q= new ArrayDeque<>();
        q.add(new Info(start,0,0));
        for (int i=0;i<N;i++){
            dist[i]=987654321;
        }
        dist[start]=0;
        while (!q.isEmpty()){
            var c= q.poll();
            int cur,cost;
            cur=c.x;
            cost=c.cost;
            for (var nxt : g2[cur]){
                int n_cost=cost+nxt.cost;
                if (dist[nxt.x]>n_cost){
                    dist[nxt.x]=n_cost;
                    q.add(new Info(nxt.x,0,n_cost));
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        st=new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        int A,B,C;
        p=new int [N];
        g2=new ArrayList[N];
        dist=new int[N];
        for (int i=0;i<N;i++){
            g2[i]=new ArrayList<>();
            p[i]=i;
            dist[i]=987654321;
        }
        for (int i=0;i<M;i++){
            st=new StringTokenizer(br.readLine());
            A=Integer.parseInt(st.nextToken());
            B=Integer.parseInt(st.nextToken());
            C=Integer.parseInt(st.nextToken());
            g.add(new Info(A,B,C));
        }
        Collections.sort(g);
        int res1,res2;
        res1=res2=0;
        for (var cur : g){
            if (uni(cur.x,cur.y)){
                g2[cur.x].add(new Info(cur.y,0,cur.cost));
                g2[cur.y].add(new Info(cur.x,0,cur.cost));
                res1+=cur.cost;
            }
        }
        go(0);
        int m=0;
        int m_idx=0;
        for (int i=0;i<N;i++){
            if (m<dist[i]){
                m=dist[i];
                m_idx=i;
            }
        }
        go(m_idx);
        for (int i=0;i<N;i++){
            res2=Math.max(res2,dist[i]);
        }
        bw.write(Integer.toString(res1)+"\n"+Integer.toString(res2));
        bw.flush();

    }


}