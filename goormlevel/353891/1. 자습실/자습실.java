import java.io.*;
import java.util.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st=new StringTokenizer(br.readLine());
		int N=Integer.parseInt(st.nextToken());
		int M=Integer.parseInt(st.nextToken());
		SortedSet<Integer> st2=new TreeSet<>();
		st=new StringTokenizer(br.readLine());
		for (int i=0;i<M;i++){
			st2.add(Integer.parseInt(st.nextToken()));
		}
		for (var cur : st2){
			bw.write(Integer.toString(cur)+" ");
		}
		bw.flush();
	}
}