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
    static ArrayList<Integer> arr= new ArrayList<>();
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        N=Integer.parseInt(br.readLine());
        StringBuilder sb;
        N+=1;

        sb= new StringBuilder(Integer.toBinaryString(N).replace('1', '7').replace('0', '4'));

        bw.write(sb.substring(1));
        bw.close();


    }


}