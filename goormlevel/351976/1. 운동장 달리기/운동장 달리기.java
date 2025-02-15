import java.io.*;
import java.util.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st= new StringTokenizer(br.readLine());
		int A,B;
		A=Integer.parseInt(st.nextToken());
		B=Integer.parseInt(st.nextToken());
		bw.write(Integer.toString((int) (A*2+(Math.PI*B))));
		bw.flush();
	}
}