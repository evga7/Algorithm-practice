import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static int N,M;
    static int res;
    static int dp[];
    static int visited[][];
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    static int dx[]={1,0,-1,0};
    static int dy[]={0,1,0,-1};
    static ArrayList<Info> arr= new ArrayList<>();
    public static class Info{
        int x,y;
        Info(int x,int y){
            this.x=x;
            this.y=y;
        }

    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st= new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        dp= new int[N+1];
        dp[0]=987654321;
        for (int i=0;i<M;i++){
            st=new StringTokenizer(br.readLine());
            int a,b;
            a=Integer.parseInt(st.nextToken());
            b=Integer.parseInt(st.nextToken());
            arr.add(new Info(a,b));
        }


        for (int i=0;i<M;i++){
            int pos=arr.get(i).x;
            int cost=arr.get(i).y;
            for (int j=N;j>=pos;j--){
                dp[j]=Math.max(dp[j],Math.min(cost,dp[j-pos]));
            }
        }
        bw.write(Integer.toString(dp[N]));
        bw.flush();
    }
}