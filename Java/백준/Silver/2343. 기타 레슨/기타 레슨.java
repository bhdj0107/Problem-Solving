import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] lectures = new int[N];
        long left = -1;
        for (int i = 0; i < N; i++) {
            lectures[i] = Integer.parseInt(st.nextToken());
            left = (long)Integer.max(lectures[i], (int)left);
        }
        left -= 1;
        long right = Integer.MAX_VALUE;

        while (true) {
            if (left == right - 1) break;
            else {
                long middle = (left + right) / 2;

                int cdCnt = 1;
                long cdStroage = middle;
                for (int i = 0; i < N; i++) {
                    int thisLecSize = lectures[i];
                    if (cdStroage < thisLecSize) {
                        cdCnt += 1; cdStroage = middle;
                    }
                    cdStroage -= thisLecSize;
                }

                if (cdCnt > M) {
                    left = middle;
                } else {
                    right = middle;
                }
            }
        }

        System.out.println(right);
    }
}