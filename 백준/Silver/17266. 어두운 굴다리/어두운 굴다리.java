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
    static int dp[][];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static int arr[];
    public static void main(String[] args) throws IOException{
        N=Integer.parseInt(br.readLine());
        M=Integer.parseInt(br.readLine());
        arr=new int [M+1];
        st=new StringTokenizer(br.readLine());
        for (int i=0;i<M;i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }
        int left=0;
        int res=Math.max(N-arr[M-1],arr[0]);
        for (int i=1;i<M;i++){
            int l=((arr[i]-left-1)/2)+1;
            res=Math.max(res,l);
            left=arr[i];

        }
        bw.write(Integer.toString(res));
        bw.flush();


    }
}