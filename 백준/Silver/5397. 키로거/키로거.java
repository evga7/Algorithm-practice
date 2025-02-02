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
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static class Info{
        int x,y;
        Info(int x,int y){
            this.x=x;
            this.y=y;
        }

    }


    public static void go(String s) throws IOException {
        List<Character> arr = new LinkedList<>();
        ListIterator<Character> it = arr.listIterator();
        int pos=0;
        int l=0;
        for (int i=0;i<s.length();i++){
            char cur = s.charAt(i);
            if (cur=='<'){
                if (it.hasPrevious()){
                    it.previous();
                }
            }
            else if (cur=='>'){
                if (it.hasNext()){
                    it.next();
                }
            }
            else if (cur=='-'){
                if (it.hasPrevious()){
                    it.previous();
                    it.remove();
                }
            }
            else{
                it.add(cur);
            }
        }
        for (Character c:arr){
            bw.write(c);
        }
        bw.write("\n");
    }
    public static void main(String[] args) throws IOException{


        N=Integer.parseInt(br.readLine());
        for (int i=0;i<N;i++){
            go(br.readLine());
        }

        bw.flush();
    }
}