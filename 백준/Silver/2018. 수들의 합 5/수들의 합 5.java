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
    static List<Integer> g[];
    static HashMap<String,Integer> m= new HashMap<>();
    public static void main(String[] args) throws IOException {
        N=Integer.parseInt(br.readLine());
        int left=0;
        int right=0;
        int s=0;
        while (right<=N){
            if (s>=N){
                if (s==N)
                    res+=1;
                left+=1;
                s-=left;
            }
            else {
                right += 1;
                s+=right;
            }
        }
        bw.write(Integer.toString(res));
        bw.flush();

    }
}