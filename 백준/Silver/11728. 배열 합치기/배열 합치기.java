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
    static int arr1[];
    static int arr2[];
    public static void main(String[] args) throws IOException {
        st=new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        arr1=new int [N];
        arr2=new int [M];
        st=new StringTokenizer(br.readLine());
        for (int i=0;i<N;i++)
            arr1[i]=Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());
        for (int i=0;i<M;i++)
            arr2[i]=Integer.parseInt(st.nextToken());
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        int idx1,idx2;
        idx1=idx2=0;
        while (idx1<N && idx2<M)
        {
            if (arr1[idx1]<arr2[idx2]) {
                bw.write(Integer.toString(arr1[idx1])+" ");
                idx1 += 1;
            }
            else{
                bw.write(Integer.toString(arr2[idx2])+" ");
                idx2 += 1;

            }
        }
        while (idx1<N) {
            bw.write(Integer.toString(arr1[idx1])+" ");
            idx1+=1;
        }
        while (idx2<M) {
            bw.write(Integer.toString(arr2[idx2])+" ");
            idx2+=1;
        }
        bw.flush();


    }


}