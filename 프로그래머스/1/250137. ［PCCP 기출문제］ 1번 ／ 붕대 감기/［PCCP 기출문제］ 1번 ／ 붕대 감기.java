class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int t=bandage[0];
        int heal=bandage[1];
        int add_heal=bandage[2];
        int cur_t=0;
        int idx=0;
        int cnt=0;
        int mx=health;
        int N=attacks.length;
        while (idx<N){
            cur_t+=1;
            if (attacks[idx][0]<=cur_t){
                health-=attacks[idx][1];
                if (health<=0){
                    health=-1;
                    break;
                }
                cnt=0;
                idx+=1;
                continue;
            }
            cnt+=1;
            if (cnt==t){
                cnt=0;
                health=Math.min(health+add_heal,mx);
            }
            health=Math.min(health+heal,mx);
        }
        return health;
    }
}