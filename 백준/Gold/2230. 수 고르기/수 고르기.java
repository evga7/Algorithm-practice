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
        st= new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        for (int i=0;i<N;i++){
            arr.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(arr);
        res=2100000000;
        int left=0;
        int right=0;

        while(left<=right && right<N){
            int s=arr.get(right)-arr.get(left);
            if (s<M){
                right+=1;
            }
            else{
                left+=1;
                res=Math.min(res,s);
            }

        }
        bw.write(Integer.toString(res));
        bw.close();
    }


}