import java.io.*;
import java.util.*;

public class Main {
    static int N,M;
    static int res;
    static ArrayList<Info> arr = new ArrayList<>();
    static ArrayList<Info2> arr2 = new ArrayList<>();
    public static void go(int idx){
        if (res==1)
            return;
        if (idx==15) {
            for (int i=0;i<6;i++){
                if (arr.get(i).win>0 || arr.get(i).draw>0 || arr.get(i).lose>0)
                    return;
            }
            res=1;
            return;
        }
        int x,y;
        x=arr2.get(idx).x;
        y=arr2.get(idx).y;
        if (arr.get(x).win>0 && arr.get(y).lose>0){
            arr.get(x).win-=1;
            arr.get(y).lose-=1;
            go(idx+1);
            arr.get(x).win+=1;
            arr.get(y).lose+=1;
        }
        if (arr.get(x).lose>0 && arr.get(y).win>0){
            arr.get(x).lose-=1;
            arr.get(y).win-=1;
            go(idx+1);
            arr.get(x).lose+=1;
            arr.get(y).win+=1;

        }
        if (arr.get(x).draw>0 && arr.get(y).draw>0){
            arr.get(x).draw-=1;
            arr.get(y).draw-=1;
            go(idx+1);
            arr.get(x).draw+=1;
            arr.get(y).draw+=1;
        }

    }
    public static class Info{
        int win;
        int draw;
        int lose;
        Info(int win, int draw,int lose){
            this.win=win;
            this.draw=draw;
            this.lose=lose;
        }
    }
    public static class Info2{
        int x,y;
        Info2(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i=0;i<4;i++) {
            Stack<Info> st2 = new Stack<>();
            arr.clear();
            res=0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 6; j++) {
                Info in=new Info(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
                arr.add(in);
            }
            for (int j=0;j<6;j++){
                for (int k=j+1;k<6;k++){
                    arr2.add(new Info2(j,k));
                }
            }
            go(0);
            bw.write(Integer.toString(res)+" ");
        }
        bw.flush();
    }
}