import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] field = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) field[i][j] = Integer.parseInt(st.nextToken());
        }
        System.out.println(get222Pooling(field, 0, 0, N));
    }

    static int get222Pooling(int[][] field, int left, int top, int N) {
        if (N == 2) {
            int[] tmpArr = new int[4];
            for (int i = 0; i < 4; i++) {
                tmpArr[i] = field[top + i / 2][left + i % 2];
            }
            Arrays.sort(tmpArr);
            return tmpArr[2];
        } else {
            int[] tmpArr = new int[4];
            int delta = N / 2;
            for (int i = 0; i < 4; i++) {
                tmpArr[i] = get222Pooling(field, left + (i % 2) * delta, top + (i / 2) * delta, N / 2);
            }
            Arrays.sort(tmpArr);
            return tmpArr[2];
        }
    }
}