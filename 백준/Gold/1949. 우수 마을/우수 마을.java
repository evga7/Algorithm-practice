import java.io.*;
import java.lang.reflect.Array;
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
    static Map<Integer,List<Integer>> g= new HashMap<>();
    public static class Info{
        int x,y;
        Info(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    public static void go(int cur){
        visited[cur]=true;
        dp[0][cur]=arr.get(cur-1);
        for (int nxt : g.get(cur)) {
            if (visited[nxt]) continue;
            go(nxt);
            dp[1][cur] += Math.max(dp[0][nxt], dp[1][nxt]);
            dp[0][cur] += dp[1][nxt];
        }

    }
    public static void main(String[] args) throws IOException{

        N=Integer.parseInt(br.readLine());

        StringTokenizer st= new StringTokenizer(br.readLine());
        visited=new boolean[N+1];
        dp=new int[2][N+1];
        for (int i=0;i<N;i++){
            arr.add(Integer.parseInt(st.nextToken()));
        }
        for (int i=0;i<N-1;i++){
            st=new StringTokenizer(br.readLine());
            int a,b;
            a=Integer.parseInt(st.nextToken());
            b=Integer.parseInt(st.nextToken());
            g.computeIfAbsent(a,k -> new ArrayList<>()).add(b);
            g.computeIfAbsent(b,k -> new ArrayList<>()).add(a);
        }
        go(1);
        bw.write(Integer.toString(Math.max(dp[1][1],dp[0][1])));
        bw.flush();
    }
}