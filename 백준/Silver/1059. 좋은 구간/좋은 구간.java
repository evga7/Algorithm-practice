import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st= new StringTokenizer(br.readLine());
        int N,M;
        N=Integer.parseInt(st.nextToken());
        st= new StringTokenizer(br.readLine());
        List<Integer> arr=new ArrayList<>();
        int flag=1;
        for (int i=0;i<N;i++){
            arr.add(Integer.parseInt(st.nextToken()));
        }
        M=Integer.parseInt(br.readLine());
        int res = 0;
        if (arr.contains(M))
            flag=0;
        if (flag==1) {
            int left = 0;
            int right = 0;
            Collections.sort(arr);
            for (int i = 0; i < N; i++) {
                int cur = arr.get(i);
                if (cur > M ) {
                    if (i-1>=0)
                        left = arr.get(i - 1);
                    right = arr.get(i);
                    break;
                }
            }

            for (int j = left + 1; j < right; j++) {
                for (int k = j + 1; k < right; k++) {
                    if (j <= M && M <= k)
                        res += 1;
                }
            }
        }
        bw.write(Integer.toString(res));
        bw.close();

    }
}
