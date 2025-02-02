import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static int N,M;
    static int res;
    static int dp[];
    static int visited[][];
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    static int dx[]={1,0,-1,0};
    static int dy[]={0,1,0,-1};
    static ArrayList<Info> arr= new ArrayList<>();
    public static class Info{
        int x,y;
        Info(int x,int y){
            this.x=x;
            this.y=y;
        }

    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        N=Integer.parseInt(br.readLine());
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i=0;i<N;i++){
            arr.add(Integer.parseInt(br.readLine()));
        }
        int res=0;
        for (int i=N-1;i>=1;i--){
            if (arr.get(i-1)>=arr.get(i)){
                int num=(arr.get(i-1)-arr.get(i))+1;
                res+=num;
                arr.set(i-1,arr.get(i-1)-num);

            }
        }
        bw.write(Integer.toString(res));
        bw.flush();
    }
}