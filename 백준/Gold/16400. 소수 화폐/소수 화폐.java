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
    static long dp[];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static boolean p[]=new boolean[40001];
    static List<Integer> arr= new ArrayList<>();
    static void go(){
        for (int i=2;i<=Math.sqrt(40000);i++){
            if (p[i])continue;
            for (int j=i*i;j<=40000;j+=i){
                p[j]=true;
            }
        }
    }
    public static void main(String[] args) throws Exception{
        N=Integer.parseInt(br.readLine());
        go();
        dp=new long[N+1];
        for (int i=2;i<=40000;i++){
            if (p[i]==false)
                arr.add(i);
        }
        dp[0]=1;
        for (int i=0;i<arr.size();i++){
            int cur=arr.get(i);
            if (cur>N)
                break;
            for (int j=cur;j<=N;j++){
                dp[j]+=dp[j-cur]%123456789;
            }
        }
        bw.write(Long.toString(dp[N]%123456789));
        bw.flush();


    }
}