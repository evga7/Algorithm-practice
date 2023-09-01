import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        String[] arr=s.split(" ");
        ArrayList<Integer> a=new ArrayList<>();
        for (int i=0;i<arr.length;i++)
        {
            a.add(Integer.parseInt(arr[i]));
        }
        Collections.sort(a);
        answer=String.valueOf(a.get(0))+' '+String.valueOf(a.get(a.size()-1));
        return answer;
    }
}