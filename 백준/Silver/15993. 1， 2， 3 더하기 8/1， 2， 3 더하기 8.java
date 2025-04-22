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
    static long dp[][];
    static ArrayList<Integer> arr = new ArrayList<>();
    static ArrayList<Integer> g[];
    static Deque<Integer> arr2 = new ArrayDeque<>();
    static boolean v[];
    public static long go(int idx,int op){
        if (idx==0){
            if ((op&1)==1)
                return 1;
            return 0;
        }
        if (dp[idx][op]!=-1)
            return dp[idx][op];
        dp[idx][op]=0;
        for (int i=1;i<=3;i++){
            if (idx-i>=0)
                dp[idx][op]+=go(idx-i,1-op)%(1000000009);

        }
        return dp[idx][op]%(1000000009);
    }

    public static void main(String[] args) throws IOException {

        N=Integer.parseInt(br.readLine());
        dp=new long [100001][2];
        for (int i=0;i<=100000;i++)
            Arrays.fill(dp[i],-1);
        for (int i=0;i<N;i++) {
            M=Integer.parseInt(br.readLine());
            bw.write(Long.toString(go(M,0)%(1000000009))+" "+Long.toString(go(M,1)%(1000000009))+"\n");
        }
        bw.close();

    }


}