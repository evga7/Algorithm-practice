import java.io.*;
import java.util.*;

public class Main {
    static int N,M,K,X;
    static int res;
    static int res2;
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
    static int dp[][][];
    static ArrayList<Integer> arr = new ArrayList<>();
    static ArrayList<Integer> g[];
    static Deque<Integer> arr2 = new ArrayDeque<>();
    static boolean v[];
    public static void go(int cnt) throws IOException {
       if (cnt==M){
           for (var cur : arr2)
               bw.write(Integer.toString(cur)+" ");
           bw.write("\n");
           return;
       }
        for (int i=0;i<N;i++){
            arr2.add(arr.get(i));
            go(cnt+1);
            arr2.pollLast();
        }

    }
    public static void main(String[] args) throws IOException {
        st= new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        st= new StringTokenizer(br.readLine());
        v= new boolean[N+1];
        for (int i=0;i<N;i++)
            arr.add(Integer.parseInt(st.nextToken()));
        Collections.sort(arr);
        go(0);
        bw.close();

    }


}