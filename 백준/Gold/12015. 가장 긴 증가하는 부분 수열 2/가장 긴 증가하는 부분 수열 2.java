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
    public static int b(int l,int num){
        int left,right,mid;
        left=0;
        right=l-1;
        while (left<=right){
            mid=left+right>>1;
            if (arr.get(mid)<num){
                left=mid+1;
            }
            else{
                right=mid-1;
            }
        }
        return left;
    }
    public static void main(String[] args) throws IOException {
        N=Integer.parseInt(br.readLine());
        st=new StringTokenizer(br.readLine());
        arr.add(-1);
        int l=1;
        for (int i=0;i<N;i++){
            int num=Integer.parseInt(st.nextToken());
            if (arr.get(l-1)<num){
                arr.add(num);
                l+=1;
            }
            else{
                int idx=b(l,num);
                arr.set(idx,num);
            }
        }
        bw.write(Integer.toString(l-1));
        bw.flush();


    }


}