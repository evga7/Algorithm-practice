import java.io.*;
import java.util.*;

public class Main {
    static int N,M;
    static int res;
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    static int dx[]={1,0,-1,0};
    static int dy[]={0,1,0,-1};
    static int dp[];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static StringBuilder sb;
    static ArrayList<Integer> arr =new ArrayList<>();
    static int b[];
    public static class Info{
        String s;
        int score;
        public Info(String s,int score){
            this.score=score;
            this.s=s;
        }
    }
    public static int go(int idx){
        if (idx==N)
            return 1;
        if (dp[idx]!=-1)
            return dp[idx];
        int ret=0;
        for (int i=idx+1;i<N;i++)
        {
            if (arr.get(i)<arr.get(idx)){
                ret=Math.max(ret,go(i)+1);
            }
        }
        dp[idx]=ret;
        return dp[idx];

    }

    public static void main(String[] args) throws IOException {
        N=Integer.parseInt(br.readLine());
        st=new StringTokenizer(br.readLine());
        dp =new int [N+1];
        Arrays.fill(dp,-1);
        for (int i=0;i<N;i++){
            arr.add(Integer.parseInt(st.nextToken()));
        }
        for (int i=0;i<N;i++){
            res=Math.max(res,go(i));
        }
        bw.write(Integer.toString(N-(res+1)));
        bw.close();
    }


}