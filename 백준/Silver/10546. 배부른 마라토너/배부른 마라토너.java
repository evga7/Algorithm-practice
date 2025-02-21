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
        for (int i=0;i<N;i++){
            String cur = br.readLine();
            m.put(cur,m.getOrDefault(cur,0)+1);
        }
        for (int i=0;i<N-1;i++){
            String cur = br.readLine();
            if (m.containsKey(cur))
                m.put(cur,m.get(cur)-1);
        }
        for (var cur :m.keySet())
            if (m.get(cur)>0)
                bw.write(cur);
        bw.flush();


    }
}