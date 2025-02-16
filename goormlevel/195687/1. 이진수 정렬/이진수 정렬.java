import java.io.*;
import java.util.*;
class Main {
	public static class Info implements Comparable<Info>{
			int x,y;
			Info(int x,int y){
					this.x=x;
					this.y=y;
			}
			@Override
			public int compareTo(Info o){
					if (this.x==o.x)
							return Integer.compare(o.y,this.y);
					return Integer.compare(o.x,this.x);
			}

	}
	public static int chk(int cur){
		int cnt=0;
		for (int i=0;i<=20;i++){
			if ((cur & (1<<i))>0)
				cnt+=1;
		}
		return cnt;
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st= new StringTokenizer(br.readLine());
		int N,M;
		N=Integer.parseInt(st.nextToken());
		M=Integer.parseInt(st.nextToken());
		st= new StringTokenizer(br.readLine());
		List<Info> arr=new ArrayList<>();
		for (int i=0;i<N;i++){
			int cur=Integer.parseInt(st.nextToken());
			arr.add(new Info(chk(cur),cur));
		}
		Collections.sort(arr);
		bw.write(Integer.toString(arr.get(M-1).y));
		bw.flush();
	}
}