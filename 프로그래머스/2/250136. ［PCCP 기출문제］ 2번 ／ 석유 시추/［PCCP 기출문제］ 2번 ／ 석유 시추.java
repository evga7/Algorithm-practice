import java.util.*;
class Solution {
    static int N,M;
    public static class info{
        int x,y;
        public info(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
    public static boolean is_inside(int x,int y,int N,int M){
        return 0<=x && x<N && 0<=y && y<M;
    }
    static HashMap<Integer,Integer>m=new HashMap<>();
    static int dx[]={0,0,1,-1};
    static int dy[]={1,-1,0,0};
    static int[][] visited;
    static int idx;
    public static void go(int sx,int sy,int land[][]){
        Queue<info> q = new LinkedList<>();
        q.add(new info(sx,sy));
        visited[sx][sy]=idx;
        int cnt=0;
        while (!q.isEmpty()){
            int x,y;
            var cur =q.poll();
            cnt+=1;
            x=cur.x;
            y=cur.y;
            for (int i=0;i<4;i++){
                int n_x=x+dx[i];
                int n_y=y+dy[i];
                if (is_inside(n_x,n_y,N,M)&& visited[n_x][n_y]==0 && land[n_x][n_y]==1)
                {
                    visited[n_x][n_y]=idx;
                    q.add(new info(n_x,n_y));
                }
            }
        }
        m.put(idx,cnt);
    }
    public int solution(int[][] land) {
        int answer = 0;
        N=land.length;
        M=land[0].length;
        idx=0;
        visited=new int [N+1][M+1];
        for (int i=0;i<N;i++){
            for (int j=0;j<M;j++){
                if (visited[i][j]==0 && land[i][j]==1){
                    idx+=1;
                    go(i,j,land);
                }
            }
        }
        for (int j=0;j<M;j++)
        {
            int s=0;
            Set<Integer>st=new HashSet<>();
            for (int i=0;i<N;i++){
                if (land[i][j]==1)
                    st.add(visited[i][j]);
            }
            for (var cur : st){
                s+=m.get(cur);
            }
            answer=Math.max(answer,s);
        }
        return answer;
    }
}