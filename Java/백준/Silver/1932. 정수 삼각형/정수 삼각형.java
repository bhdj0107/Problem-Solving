import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] alArray = new int[N][];
        int[][] sumAlArray = new int[N][];
        for (int i = 0; i < N; i++) {
            alArray[i] = new int[i + 1];
            sumAlArray[i] = new int[i + 1];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < i + 1; j++) {
                alArray[i][j] = Integer.parseInt(st.nextToken());
                sumAlArray[i][j] = -1;
            }
        }

        sumAlArray[0][0] = alArray[0][0];
        for (int i = 0; i < N - 1; i++) {
            for (int j = 0; j < i + 1; j++) {
                for (int k = 0; k < 2; k++)
                    sumAlArray[i + 1][j + k] = Integer.max(sumAlArray[i + 1][j + k], alArray[i + 1][j + k] + sumAlArray[i][j]);
            }
        }

        int ans = -1;
        for (int i = 0; i < N; i++) ans = Integer.max(ans, sumAlArray[N - 1][i]);
        System.out.println(ans);
    }
}