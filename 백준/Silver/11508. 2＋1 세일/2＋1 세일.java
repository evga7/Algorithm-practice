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


    public static void main(String[] args) throws IOException {
        N=Integer.parseInt(br.readLine());
        for (int i=0;i<N;i++){
            arr.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(arr);
        res=0;
        int cnt=0;
        for (int i=N-1;i>=0;i--){
            cnt+=1;
            if (cnt==3){
                cnt=0;
                continue;
            }
            res+=arr.get(i);
        }
        bw.write(Integer.toString(res));
        bw.close();
    }


}