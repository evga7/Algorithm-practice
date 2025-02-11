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
    static ArrayList<String> arr= new ArrayList<>();
    public static class Info{
        int x,y;
        Info(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    public static boolean chk(String s){
        int f,f2;
        f=0;
        f2=0;
        for (var cur : s.toCharArray()){
            if (cur=='a' || cur=='e'|| cur=='i'||cur=='o'||cur=='u'){
                f=1;
            }
            else{
                f2+=1;
            }
            if (f>0 && f2>1)
                return true;
        }
        return false;
    }
    public static void go(int idx,int cnt,String s) throws IOException{
        if (cnt==N){
            if (chk(s))
                bw.write(s+"\n");
            return;
        }
        for (int i=idx;i<M;i++){
            go(i+1,cnt+1,s+arr.get(i));
        }

    }
    public static void main(String[] args) throws IOException{
        StringTokenizer st= new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        visited= new boolean[M+1];
        st= new StringTokenizer(br.readLine());
        for (int i=0;i<M;i++){
            arr.add(st.nextToken());
        }
        Collections.sort(arr);
        go(0,0,"");
        bw.flush();
    }
}