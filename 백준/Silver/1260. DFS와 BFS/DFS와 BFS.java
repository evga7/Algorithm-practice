import java.io.*;
import java.util.*;

public class Main {

    static int[][] arr;
    static boolean visited[];
    static int N;
    public static void bfs(int start){
        Queue<Integer> q= new LinkedList<>();
        q.add(start);
        visited[start]=true;
        while (!q.isEmpty())
        {
            int cur=q.poll();
            System.out.printf("%d ",cur);
            for (int i=1;i<=N;i++)
            {
                if (arr[cur][i]==1 && visited[i]==false){
                    visited[i]=true;
                    q.add(i);
                }
            }
        }

    }
    public static void dfs(int cur){
        visited[cur]=true;
        System.out.printf("%d ",cur);
        for (int i=1;i<=N;i++)
        {
            if (arr[cur][i]==1 && visited[i]==false)
            {
                dfs(i);
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        int M,V;
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        V=Integer.parseInt(st.nextToken());
        arr=new int[N+1][N+1];

        for (int i=0;i<M;i++)
        {
            StringTokenizer str= new StringTokenizer(br.readLine());
            int q,w;
            q=Integer.parseInt(str.nextToken());
            w=Integer.parseInt(str.nextToken());
            arr[q][w]=1;
            arr[w][q]=1;
        }
        visited=new boolean[N+1];
        dfs(V);
        System.out.println();
        visited=new boolean[N+1];
        bfs(V);
    }
}