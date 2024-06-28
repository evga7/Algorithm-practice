import java.io.*;
import java.util.*;

public class Main {

    static List<List<Integer>> g;
    static int dist[];
    static int N,M,K,X;
    static class info{
        private int cost;
        private int cur;
        public info(int cost,int cur){
            this.cost=cost;
            this.cur=cur;
        }
    }
    public static void go() throws IOException {
        Queue<info> q=new LinkedList<>();
        q.add(new info(0,X));
        dist[X]=0;
        while (!q.isEmpty())
        {
            info i1=q.poll();
            int cost,cur;
            cost=i1.cost;
            cur=i1.cur;
            if (dist[cur]<cost)continue;
            for (int nxt : g.get(cur))
            {
                if (dist[nxt]>cost+1)
                {
                    dist[nxt]=cost+1;
                    q.add(new info(cost+1,nxt));
                }
            }
        }
        boolean f=false;
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i=1;i<=N;i++)
        {
            if (dist[i]==K){
                bw.write(String.valueOf(i)+"\n");
                f=true;
            }
        }
        if (f==false) {
            bw.write("-1");
        }
        bw.flush();
        bw.close();

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        K=Integer.parseInt(st.nextToken());
        X=Integer.parseInt(st.nextToken());
        dist=new int[N+1];
        Arrays.fill(dist,987654321);
        g= new ArrayList<>();
        for (int i=0;i<N+1;i++)
            g.add(new ArrayList<>());

        for (int i=0;i<M;i++)
        {
            StringTokenizer str= new StringTokenizer(br.readLine());
            int q,w;
            q=Integer.parseInt(str.nextToken());
            w=Integer.parseInt(str.nextToken());
            g.get(q).add(w);
        }
        go();
    }
}