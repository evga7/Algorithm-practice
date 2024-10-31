import java.io.*;
import java.util.*;

public class Main {
    static int visited[][];
    static int arr[][];
    static int dx[]={0,0,-1,1};
    static int dy[]={-1,1,0,0};
    static int N;
    static List<Integer>v=new ArrayList<>();
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s=br.readLine();
        String s2=br.readLine();
        int idx=0;
        int l=s2.length();
        for (int i=0;i<s.length();i++)
        {
            char cur=s.charAt(i);
            char cur2=s2.charAt(idx);
            idx+=1;
            idx%=l;
            if (cur==' ') {
                bw.write(cur);
                continue;
            }
            int num=cur2-'a';
            int num2=cur-'a';
            num2=((num2-num)+26)%26;
            int c='a'+num2-1;
            if (c==96)
                c=122;
            bw.write(c);
        }
        bw.flush();
        bw.close();
    }
}
