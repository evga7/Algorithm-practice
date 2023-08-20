import java.util.*;
class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        Arrays.sort(A);
        Arrays.sort(B);
        int num=0;
        for (int i = 0; i < B.length; i++) {
            num=Arrays.binarySearch(B,num,B.length, A[i]+1);
            if (num<0)
                num*=-1;
            if (num>B.length)break;
            answer+=1;
        }
        return answer;
    }
}