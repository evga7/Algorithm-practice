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
    static List<Integer> g[];
    public static boolean chk(String s){
        int left=0;
        int right=s.length()-1;
        while (s.charAt(left)==s.charAt(right) && left<right){
            left+=1;
            right-=1;
        }
        return left>=right;
    }
    public static void main(String[] args) throws IOException {
        if (chk(br.readLine()))
            bw.write("1");
        else
            bw.write("0");
        bw.flush();

    }
}