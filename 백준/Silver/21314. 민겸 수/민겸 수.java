import java.io.*;
import java.util.*;

public class Main {
    static int N,M;
    static int res;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str=br.readLine();
        StringBuilder mx= new StringBuilder();
        StringBuilder mi= new StringBuilder();
        int cnt=0;
        for (int i=0;i<str.length();i++){
            if (str.charAt(i)=='M'){
                if (mi.length() >0&&mi.charAt(mi.length()-1)!='5')
                    mi.append("0");
                else
                    mi.append("1");
                cnt+=1;
            }
            else{
                mx.append("5");
                for (int j=0;j<cnt;j++)
                    mx.append("0");
                cnt=0;
                mi.append("5");
            }
        }

        if (cnt>0){
            for (int j=0;j<cnt;j++)
                mx.append("1");
        }
        bw.write(mx.toString()+"\n"+mi.toString());
        bw.flush();
    }
}