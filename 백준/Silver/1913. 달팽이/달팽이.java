import java.io.*;
import java.util.*;

public class Main {
    static int N,M;
    static int res;
    static int dp[][];
    static int visited[][];
    static int arr[][];
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    static int dx[]={1,0,-1,0};
    static int dy[]={0,1,0,-1};
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
        M=Integer.parseInt(br.readLine());
        int num=N*N;
        arr = new int[N][N];
        int x,y;
        x=0;
        y=0;
        int dir=0;
        Map<Integer,Info> m= new HashMap();
        while (true){
            arr[x][y]=num;
            m.put(num,new Info(x+1,y+1));
            num-=1;
            if (num==0) {
                break;
            }
            int n_x=x+dx[dir];
            int n_y=y+dy[dir];
            while (!is_inside(n_x,n_y,N,N) || arr[n_x][n_y]>0){
                dir+=1;
                dir%=4;
                n_x=x+dx[dir];
                n_y=y+dy[dir];
            }
            x=n_x;
            y=n_y;

        }
        for (int i=0;i<N;i++){
            for (int j=0;j<N;j++){
                bw.write(Integer.toString(arr[i][j])+" ");
            }
            bw.write("\n");
        }
        bw.write(Integer.toString(m.get(M).x)+" "+Integer.toString(m.get(M).y));
        bw.flush();
    }
}