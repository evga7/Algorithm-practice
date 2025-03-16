import java.io.*;
import java.util.*;

public class Main {
    static int N,M;
    static long res;
    static boolean visited[];
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    static int dx[]={1,0,-1,0};
    static int dy[]={0,1,0,-1};
    static int dp[][];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static ArrayList<Info> arr= new ArrayList<>();
    static ArrayList<Info2> arr2= new ArrayList<>();
    static StringTokenizer st;
    public static class Info implements Comparable<Info>{
        int x,y;
        public Info(int x,int y){
            this.x=x;
            this.y=y;
        }
        public int compareTo(Info o){
            return Integer.compare(this.x,o.x);
        }
    }
    public static class Info2 implements Comparable<Info2>{
        int x,y;
        public Info2(int x,int y){
            this.x=x;
            this.y=y;
        }
        public int compareTo(Info2 o){
            return Integer.compare(this.y,o.y);
        }
    }

    public static void main(String[] args) throws IOException {
        N=Integer.parseInt(br.readLine());
        int A,B;
        for (int i=0;i<N;i++){
            st =new StringTokenizer(br.readLine());
            A=Integer.parseInt(st.nextToken());
            B=Integer.parseInt(st.nextToken());
            arr.add(new Info(A,B));
            arr2.add(new Info2(A,B));
        }
        res=0;
        Collections.sort(arr);
        Collections.sort(arr2);
        int x,y;
        x=arr.get((int)N/2).x;
        y=arr2.get((int)N/2).y;
        for (int i=0;i<N;i++){
            res+=Math.abs(x-arr.get(i).x);
            res+=Math.abs(y-arr.get(i).y);
        }
        bw.write(Long.toString(res));
        bw.flush();

    }


}