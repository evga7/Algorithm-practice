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
    static Map<Integer,List<Integer>> g= new HashMap<>();
    public static class Info{
        int x,y;
        Info(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    public static void main(String[] args) throws IOException{


        while (true){
            String str=br.readLine();
            Stack<Character> st=new Stack<>();
            if (str.equals(".")){
                break;
            }
            boolean f=true;
            for (char c: str.toCharArray()){
                if (c=='(' || c=='['){
                    st.add(c);
                }
                else{
                    if (c==')'){
                        if (!st.empty() && st.peek()=='(')
                            st.pop();
                        else{
                            f=false;
                            break;
                        }
                    }
                    else if (c==']'){
                        if (!st.empty() && st.peek()=='[')
                            st.pop();
                        else{
                            f=false;
                            break;
                        }
                    }
                }
            }
            if (f && st.empty()){
                bw.write("yes\n");
            }
            else
                bw.write("no\n");

        }

        bw.flush();
    }
}