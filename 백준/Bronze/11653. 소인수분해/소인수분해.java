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


    public static void main(String[] args) throws IOException {

        N=Integer.parseInt(br.readLine());
        while (N>1){
            for (int i=2;i<=N;i++){
                if (N%i==0) {
                    bw.write(Integer.toString(i)+"\n");
                    N/=i;
                    break;
                }
            }
        }
        bw.close();

    }


}