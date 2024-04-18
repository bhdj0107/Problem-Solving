import java.io.*;
import java.util.*;

public class Main {
    static HashMap<Integer, Boolean> isAbleNum = new HashMap<>();
    static int minimumDistance;
    static int dst;
    static int[] outputArray = new int[7];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        dst = Integer.parseInt(br.readLine());
        minimumDistance = Math.abs(dst - 100);
        int M = Integer.parseInt(br.readLine());
        
        for (int i = -1; i < 11; i++) isAbleNum.put(i, true);

        if (M > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < M; i++) isAbleNum.put(Integer.parseInt(st.nextToken()), false);
        }

        if (isAbleNum.get(0)) dfs(0);
        else {
            for (int i = 6; i >= 0; i--) {
                dfs(i);
            }
        }
        System.out.println(minimumDistance);
        
    }

    static void dfs(int D) {
        if (D == 7) {
            int currentNum = 0;
            for (int i = 0; i < 7; i++) {
                currentNum += outputArray[i] * (int)Math.pow(10, 6 - i);
            }
            int currentLen = Integer.toString(currentNum).length();
            minimumDistance = Integer.min(minimumDistance, (int)Math.abs(dst - currentNum) + currentLen);
        } else {
            for (int i = 0; i < 10; i++) {
                if (isAbleNum.get(i)) {
                    outputArray[D] = i;
                    dfs(D + 1);
                }
            }
        }
    }
}