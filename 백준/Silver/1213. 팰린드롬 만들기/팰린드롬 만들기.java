import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        
        // 문자 개수 세기
        Map<Character, Integer> counter = new TreeMap<>();
        for (char ch : input.toCharArray()) {
            counter.put(ch, counter.getOrDefault(ch, 0) + 1);
        }
        
        StringBuilder leftPart = new StringBuilder();
        StringBuilder rightPart = new StringBuilder();
        String middleChar = "";
        int oddCount = 0;

        // 문자와 개수 확인
        for (Map.Entry<Character, Integer> entry : counter.entrySet()) {
            char ch = entry.getKey();
            int count = entry.getValue();
            
            // 홀수 개수가 두 개 이상이면 팰린드롬 불가능
            if (count % 2 == 1) {
                middleChar = String.valueOf(ch);
                oddCount++;
                if (oddCount > 1) {
                    System.out.println("I'm Sorry Hansoo");
                    return;
                }
            }
            
            // 문자열 반쪽 생성
            for (int i = 0; i < count / 2; i++) {
                leftPart.append(ch);
            }
        }

        rightPart.append(leftPart).reverse();
        System.out.println(leftPart.toString() + middleChar + rightPart.toString());
    }
}