import java.io.*;
import java.util.*;
class Main {
	static long X,A,B,T;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st= new StringTokenizer(br.readLine());
		X=Integer.parseInt(st.nextToken());
		A=Integer.parseInt(st.nextToken());
		B=Integer.parseInt(st.nextToken());
		T=Integer.parseInt(st.nextToken());
		B-=A;
		bw.write(Long.toString(X+(B*T)));
		bw.flush();
	}
}