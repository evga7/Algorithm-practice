import java.io.*;
import java.util.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st= new StringTokenizer(br.readLine());
		int A,B,C,D;
		A=Integer.parseInt(st.nextToken());
		B=Integer.parseInt(st.nextToken());
		C=Integer.parseInt(st.nextToken());
		D=Integer.parseInt(st.nextToken());
		if (A*B>C*D){
			bw.write("G");
		}
		else if (A*B<C*D)
		{
			bw.write("B");
		}
		else
			bw.write("D");
		bw.flush();
	}
}