class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {0,0};
        int left=0;
        int right=0;
        int N=sequence.length;
        int S=0;
        int res=987654321;
        int r_left=0;
        int r_right=0;
        while (left<=right && right<=N)
        {
            while (S>=k)
            {
                if (S==k){
                    if (res>right-left)
                    {
                        res=right-left;
                        r_left=left;
                        r_right=right-1;
                    }
                }
                S-=sequence[left];
                left+=1;
            }
            if (right==N)
                break;
            S+=sequence[right];
            right+=1;
            
        }
        answer[0]=r_left;
        answer[1]=r_right;
        return answer;
    }
}